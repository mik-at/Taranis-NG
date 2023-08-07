import { defineStore } from 'pinia'
import { getLocalConfig } from '@/services/config'
import { ref, computed } from 'vue'

export const useMainStore = defineStore(
  'main',
  () => {
    const user = ref({
      id: '',
      name: '',
      organization_name: '',
      permissions: []
    })
    const vertical_view = ref(false)
    const itemCountTotal = ref(0)
    const itemCountFiltered = ref(0)
    const drawerVisible = ref(true)
    const coreAPIURL = ref('/api')
    const buildDate = ref(new Date().toISOString())
    const notification = ref({ message: '', type: '', show: false })

    // Getters
    const getItemCount = computed(() => {
      return { total: itemCountTotal.value, filtered: itemCountFiltered.value }
    })

    const updateFromLocalConfig = async () => {
      const config = await getLocalConfig()
      coreAPIURL.value = config.CORE_API ?? '/api'
      buildDate.value = config.BUILD_DATE ?? new Date().toISOString()
    }

    // Actions
    const toggleDrawer = () => {
      drawerVisible.value = !drawerVisible.value
    }

    const resetItemCount = () => {
      itemCountTotal.value = 0
      itemCountFiltered.value = 0
    }
    return {
      user,
      vertical_view,
      drawerVisible,
      itemCountTotal,
      itemCountFiltered,
      coreAPIURL,
      buildDate,
      notification,
      getItemCount,
      updateFromLocalConfig,
      toggleDrawer,
      resetItemCount
    }
  },
  {
    persist: true
  }
)
