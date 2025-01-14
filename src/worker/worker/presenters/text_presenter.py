from .base_presenter import BasePresenter


class TextPresenter(BasePresenter):
    type = "TEXT_PRESENTER"
    name = "TEXT Presenter"
    description = "Presenter for generating text documents"

    def generate(self, presenter_input, template) -> dict[str, str]:
        return super().generate(presenter_input, template)
