"""initial state

Revision ID: e2539f49e3c1
Revises:
Create Date: 2023-07-05 15:57:00.141117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e2539f49e3c1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "acl_entry",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column(
            "item_type",
            sa.Enum(
                "COLLECTOR",
                "OSINT_SOURCE",
                "OSINT_SOURCE_GROUP",
                "WORD_LIST",
                "REPORT_ITEM",
                "REPORT_ITEM_TYPE",
                "PRODUCT_TYPE",
                "DELEGATION",
                name="itemtype",
            ),
            nullable=True,
        ),
        sa.Column("item_id", sa.String(length=64), nullable=True),
        sa.Column("everyone", sa.Boolean(), nullable=True),
        sa.Column("see", sa.Boolean(), nullable=True),
        sa.Column("access", sa.Boolean(), nullable=True),
        sa.Column("modify", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "address",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("street", sa.String(), nullable=True),
        sa.Column("city", sa.String(), nullable=True),
        sa.Column("zip", sa.String(), nullable=True),
        sa.Column("country", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "attribute",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column(
            "type",
            sa.Enum(
                "STRING",
                "NUMBER",
                "BOOLEAN",
                "RADIO",
                "ENUM",
                "TEXT",
                "RICH_TEXT",
                "DATE",
                "TIME",
                "DATE_TIME",
                "LINK",
                "ATTACHMENT",
                "TLP",
                "CPE",
                "CVE",
                "CVSS",
                name="attributetype",
            ),
            nullable=True,
        ),
        sa.Column("default_value", sa.String(), nullable=True),
        sa.Column("validator", sa.Enum("NONE", "EMAIL", "NUMBER", "RANGE", "REGEXP", name="attributevalidator"), nullable=True),
        sa.Column("validator_parameter", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "bot",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("type", sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "bots_node",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("api_url", sa.String(), nullable=False),
        sa.Column("api_key", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "collector",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("type", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "collectors_node",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("api_url", sa.String(), nullable=False),
        sa.Column("api_key", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "osint_source_group",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("default", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "parameter",
        sa.Column("key", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("type", sa.Enum("STRING", "NUMBER", "BOOLEAN", "LIST", name="parametertype"), nullable=True),
        sa.PrimaryKeyConstraint("key"),
    )
    op.create_table(
        "permission",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "presenters_node",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("api_url", sa.String(), nullable=False),
        sa.Column("api_key", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "publishers_node",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("api_url", sa.String(), nullable=False),
        sa.Column("api_key", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "remote_access",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.Column("connected", sa.Boolean(), nullable=True),
        sa.Column("access_key", sa.String(), nullable=True),
        sa.Column("event_id", sa.String(length=64), nullable=True),
        sa.Column("last_synced_news_items", sa.DateTime(), nullable=True),
        sa.Column("last_synced_report_items", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("access_key"),
        sa.UniqueConstraint("event_id"),
    )
    op.create_table(
        "report_item_type",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "role",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "tag_cloud",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("word", sa.String(), nullable=True),
        sa.Column("word_quantity", sa.BigInteger(), nullable=True),
        sa.Column("collected", sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "token_blacklist",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("token", sa.String(), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_profile",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("spellcheck", sa.Boolean(), nullable=True),
        sa.Column("dark_theme", sa.Boolean(), nullable=True),
        sa.Column("language", sa.String(length=2), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "word_list",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("use_for_stop_words", sa.Boolean(), nullable=True),
        sa.Column("link", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "acl_entry_role",
        sa.Column("acl_entry_id", sa.Integer(), nullable=False),
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["acl_entry_id"],
            ["acl_entry.id"],
        ),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["role.id"],
        ),
        sa.PrimaryKeyConstraint("acl_entry_id", "role_id"),
    )
    op.create_table(
        "attribute_enum",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("index", sa.Integer(), nullable=True),
        sa.Column("value", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("imported", sa.Boolean(), nullable=True),
        sa.Column("attribute_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["attribute_id"], ["attribute.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "attribute_group",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("section", sa.Integer(), nullable=True),
        sa.Column("section_title", sa.String(), nullable=True),
        sa.Column("index", sa.Integer(), nullable=True),
        sa.Column("report_item_type_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["report_item_type_id"],
            ["report_item_type.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "collector_parameter",
        sa.Column("collector_id", sa.String(), nullable=False),
        sa.Column("parameter_id", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["collector_id"], ["collector.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["parameter_id"], ["parameter.key"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("collector_id", "parameter_id"),
    )
    op.create_table(
        "hotkey",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("key_code", sa.Integer(), nullable=True),
        sa.Column("key", sa.String(), nullable=True),
        sa.Column("alias", sa.String(), nullable=True),
        sa.Column("user_profile_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_profile_id"],
            ["user_profile.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "news_item_aggregate",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("read", sa.Boolean(), nullable=True),
        sa.Column("important", sa.Boolean(), nullable=True),
        sa.Column("likes", sa.Integer(), nullable=True),
        sa.Column("dislikes", sa.Integer(), nullable=True),
        sa.Column("relevance", sa.Integer(), nullable=True),
        sa.Column("comments", sa.String(), nullable=True),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("osint_source_group_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["osint_source_group_id"],
            ["osint_source_group.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "organization",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("address_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["address_id"],
            ["address.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "osint_source",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("collector_id", sa.String(), nullable=True),
        sa.Column("modified", sa.DateTime(), nullable=True),
        sa.Column("last_collected", sa.DateTime(), nullable=True),
        sa.Column("last_attempted", sa.DateTime(), nullable=True),
        sa.Column("state", sa.SmallInteger(), nullable=True),
        sa.Column("last_error_message", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["collector_id"],
            ["collector.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "parameter_value",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("value", sa.String(), nullable=False),
        sa.Column("parameter_key", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parameter_key"],
            ["parameter.key"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "presenter",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("node_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["node_id"],
            ["presenters_node.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "publisher",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("node_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["node_id"],
            ["publishers_node.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "remote_access_report_item_type",
        sa.Column("remote_access_id", sa.Integer(), nullable=False),
        sa.Column("report_item_type_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["remote_access_id"],
            ["remote_access.id"],
        ),
        sa.ForeignKeyConstraint(
            ["report_item_type_id"],
            ["report_item_type.id"],
        ),
        sa.PrimaryKeyConstraint("remote_access_id", "report_item_type_id"),
    )
    op.create_table(
        "remote_node",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.Column("remote_url", sa.String(), nullable=True),
        sa.Column("events_url", sa.String(), nullable=True),
        sa.Column("access_key", sa.String(), nullable=True),
        sa.Column("sync_news_items", sa.Boolean(), nullable=True),
        sa.Column("osint_source_group_id", sa.String(), nullable=True),
        sa.Column("sync_report_items", sa.Boolean(), nullable=True),
        sa.Column("event_id", sa.String(length=64), nullable=True),
        sa.Column("last_synced_news_items", sa.DateTime(), nullable=True),
        sa.Column("last_synced_report_items", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["osint_source_group_id"],
            ["osint_source_group.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("event_id"),
    )
    op.create_table(
        "role_permission",
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.Column("permission_id", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["permission_id"],
            ["permission.id"],
        ),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["role.id"],
        ),
        sa.PrimaryKeyConstraint("role_id", "permission_id"),
    )
    op.create_table(
        "word_list_entry",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("value", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("word_list_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["word_list_id"],
            ["word_list.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "asset_group",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("organization_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organization.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "attribute_group_item",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("index", sa.Integer(), nullable=True),
        sa.Column("min_occurrence", sa.Integer(), nullable=True),
        sa.Column("max_occurrence", sa.Integer(), nullable=True),
        sa.Column("attribute_group_id", sa.Integer(), nullable=True),
        sa.Column("attribute_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["attribute_group_id"],
            ["attribute_group.id"],
        ),
        sa.ForeignKeyConstraint(
            ["attribute_id"],
            ["attribute.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "bot_parameter_value",
        sa.Column("bot_id", sa.String(), nullable=False),
        sa.Column("parameter_value_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["bot_id"],
            ["bot.id"],
        ),
        sa.ForeignKeyConstraint(
            ["parameter_value_id"],
            ["parameter_value.id"],
        ),
        sa.PrimaryKeyConstraint("bot_id", "parameter_value_id"),
    )
    op.create_table(
        "news_item_aggregate_search_index",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data", sa.String(), nullable=True),
        sa.Column("news_item_aggregate_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["news_item_aggregate_id"],
            ["news_item_aggregate.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "news_item_attribute",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("key", sa.String(), nullable=False),
        sa.Column("value", sa.String(), nullable=False),
        sa.Column("binary_mime_type", sa.String(), nullable=True),
        sa.Column("binary_data", sa.LargeBinary(), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("remote_node_id", sa.Integer(), nullable=True),
        sa.Column("remote_user", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["remote_node_id"],
            ["remote_node.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "news_item_data",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("hash", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("review", sa.String(), nullable=True),
        sa.Column("author", sa.String(), nullable=True),
        sa.Column("source", sa.String(), nullable=True),
        sa.Column("link", sa.String(), nullable=True),
        sa.Column("language", sa.String(), nullable=True),
        sa.Column("content", sa.String(), nullable=True),
        sa.Column("collected", sa.DateTime(), nullable=True),
        sa.Column("published", sa.DateTime(), nullable=True),
        sa.Column("updated", sa.DateTime(), nullable=True),
        sa.Column("osint_source_id", sa.String(), nullable=True),
        sa.Column("remote_source", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["osint_source_id"],
            ["osint_source.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "news_item_tag",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("tag_type", sa.String(length=255), nullable=True),
        sa.Column("n_i_a_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["n_i_a_id"],
            ["news_item_aggregate.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "osint_source_group_osint_source",
        sa.Column("osint_source_group_id", sa.String(), nullable=False),
        sa.Column("osint_source_id", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["osint_source_group_id"], ["osint_source_group.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["osint_source_id"], ["osint_source.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("osint_source_group_id", "osint_source_id"),
    )
    op.create_table(
        "osint_source_parameter_value",
        sa.Column("osint_source_id", sa.String(), nullable=False),
        sa.Column("parameter_value_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["osint_source_id"], ["osint_source.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["parameter_value_id"], ["parameter_value.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("osint_source_id", "parameter_value_id"),
    )
    op.create_table(
        "osint_source_word_list",
        sa.Column("osint_source_id", sa.String(), nullable=False),
        sa.Column("word_list_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["osint_source_id"], ["osint_source.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["word_list_id"],
            ["word_list.id"],
        ),
        sa.PrimaryKeyConstraint("osint_source_id", "word_list_id"),
    )
    op.create_table(
        "presenter_parameter",
        sa.Column("presenter_id", sa.String(), nullable=False),
        sa.Column("parameter_key", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["parameter_key"],
            ["parameter.key"],
        ),
        sa.ForeignKeyConstraint(
            ["presenter_id"],
            ["presenter.id"],
        ),
        sa.PrimaryKeyConstraint("presenter_id", "parameter_key"),
    )
    op.create_table(
        "product_type",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=64), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("presenter_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["presenter_id"],
            ["presenter.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    op.create_table(
        "publisher_parameter",
        sa.Column("publisher_id", sa.String(), nullable=False),
        sa.Column("parameter_key", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["parameter_key"],
            ["parameter.key"],
        ),
        sa.ForeignKeyConstraint(
            ["publisher_id"],
            ["publisher.id"],
        ),
        sa.PrimaryKeyConstraint("publisher_id", "parameter_key"),
    )
    op.create_table(
        "publisher_preset",
        sa.Column("id", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("publisher_id", sa.String(), nullable=True),
        sa.Column("use_for_notifications", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["publisher_id"],
            ["publisher.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "remote_access_osint_source",
        sa.Column("remote_access_id", sa.Integer(), nullable=False),
        sa.Column("osint_source_id", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["osint_source_id"],
            ["osint_source.id"],
        ),
        sa.ForeignKeyConstraint(
            ["remote_access_id"],
            ["remote_access.id"],
        ),
        sa.PrimaryKeyConstraint("remote_access_id", "osint_source_id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=64), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=True),
        sa.Column("organization_id", sa.Integer(), nullable=True),
        sa.Column("profile_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organization.id"],
        ),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["user_profile.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "acl_entry_user",
        sa.Column("acl_entry_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["acl_entry_id"],
            ["acl_entry.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("acl_entry_id", "user_id"),
    )
    op.create_table(
        "asset",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("serial", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("asset_group_id", sa.String(), nullable=True),
        sa.Column("vulnerabilities_count", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["asset_group_id"],
            ["asset_group.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "news_item",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("read", sa.Boolean(), nullable=True),
        sa.Column("important", sa.Boolean(), nullable=True),
        sa.Column("likes", sa.Integer(), nullable=True),
        sa.Column("dislikes", sa.Integer(), nullable=True),
        sa.Column("relevance", sa.Integer(), nullable=True),
        sa.Column("news_item_data_id", sa.String(), nullable=True),
        sa.Column("news_item_aggregate_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["news_item_aggregate_id"],
            ["news_item_aggregate.id"],
        ),
        sa.ForeignKeyConstraint(
            ["news_item_data_id"],
            ["news_item_data.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "news_item_aggregate_news_item_attribute",
        sa.Column("news_item_aggregate_id", sa.Integer(), nullable=False),
        sa.Column("news_item_attribute_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["news_item_aggregate_id"],
            ["news_item_aggregate.id"],
        ),
        sa.ForeignKeyConstraint(
            ["news_item_attribute_id"],
            ["news_item_attribute.id"],
        ),
        sa.PrimaryKeyConstraint("news_item_aggregate_id", "news_item_attribute_id"),
    )
    op.create_table(
        "news_item_data_news_item_attribute",
        sa.Column("news_item_data_id", sa.String(), nullable=False),
        sa.Column("news_item_attribute_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["news_item_attribute_id"],
            ["news_item_attribute.id"],
        ),
        sa.ForeignKeyConstraint(
            ["news_item_data_id"],
            ["news_item_data.id"],
        ),
        sa.PrimaryKeyConstraint("news_item_data_id", "news_item_attribute_id"),
    )
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("product_type_id", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["product_type_id"],
            ["product_type.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "product_type_parameter_value",
        sa.Column("product_type_id", sa.Integer(), nullable=False),
        sa.Column("parameter_value_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["parameter_value_id"],
            ["parameter_value.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_type_id"],
            ["product_type.id"],
        ),
        sa.PrimaryKeyConstraint("product_type_id", "parameter_value_id"),
    )
    op.create_table(
        "publisher_preset_parameter_value",
        sa.Column("publisher_preset_id", sa.String(), nullable=False),
        sa.Column("parameter_value_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["parameter_value_id"],
            ["parameter_value.id"],
        ),
        sa.ForeignKeyConstraint(
            ["publisher_preset_id"],
            ["publisher_preset.id"],
        ),
        sa.PrimaryKeyConstraint("publisher_preset_id", "parameter_value_id"),
    )
    op.create_table(
        "report_item",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uuid", sa.String(length=64), nullable=True),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("title_prefix", sa.String(), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("last_updated", sa.DateTime(), nullable=True),
        sa.Column("completed", sa.Boolean(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("remote_user", sa.String(), nullable=True),
        sa.Column("report_item_type_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["report_item_type_id"],
            ["report_item_type.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_permission",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("permission_id", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["permission_id"],
            ["permission.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("user_id", "permission_id"),
    )
    op.create_table(
        "user_role",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("role_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["role.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("user_id", "role_id"),
    )
    op.create_table(
        "asset_cpe",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("value", sa.String(), nullable=True),
        sa.Column("asset_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["asset_id"],
            ["asset.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "asset_vulnerability",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("solved", sa.Boolean(), nullable=True),
        sa.Column("asset_id", sa.Integer(), nullable=True),
        sa.Column("report_item_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["asset_id"],
            ["asset.id"],
        ),
        sa.ForeignKeyConstraint(
            ["report_item_id"],
            ["report_item.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "news_item_vote",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("like", sa.Boolean(), nullable=True),
        sa.Column("dislike", sa.Boolean(), nullable=True),
        sa.Column("news_item_id", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("remote_node_id", sa.Integer(), nullable=True),
        sa.Column("remote_user", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["news_item_id"],
            ["news_item.id"],
        ),
        sa.ForeignKeyConstraint(
            ["remote_node_id"],
            ["remote_node.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "product_report_item",
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("report_item_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.ForeignKeyConstraint(
            ["report_item_id"],
            ["report_item.id"],
        ),
        sa.PrimaryKeyConstraint("product_id", "report_item_id"),
    )
    op.create_table(
        "report_item_attribute",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("value", sa.String(), nullable=False),
        sa.Column("binary_mime_type", sa.String(), nullable=True),
        sa.Column("binary_data", sa.LargeBinary(), nullable=True),
        sa.Column("binary_description", sa.String(), nullable=True),
        sa.Column("attribute_group_item_id", sa.Integer(), nullable=True),
        sa.Column("report_item_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["attribute_group_item_id"],
            ["attribute_group_item.id"],
        ),
        sa.ForeignKeyConstraint(
            ["report_item_id"],
            ["report_item.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "report_item_cpe",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("value", sa.String(), nullable=True),
        sa.Column("report_item_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["report_item_id"],
            ["report_item.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "report_item_news_item_aggregate",
        sa.Column("report_item_id", sa.Integer(), nullable=False),
        sa.Column("news_item_aggregate_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["news_item_aggregate_id"],
            ["news_item_aggregate.id"],
        ),
        sa.ForeignKeyConstraint(
            ["report_item_id"],
            ["report_item.id"],
        ),
        sa.PrimaryKeyConstraint("report_item_id", "news_item_aggregate_id"),
    )
    op.create_table(
        "report_item_remote_report_item",
        sa.Column("report_item_id", sa.Integer(), nullable=False),
        sa.Column("remote_report_item_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["remote_report_item_id"],
            ["report_item.id"],
        ),
        sa.ForeignKeyConstraint(
            ["report_item_id"],
            ["report_item.id"],
        ),
        sa.PrimaryKeyConstraint("report_item_id", "remote_report_item_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("report_item_remote_report_item")
    op.drop_table("report_item_news_item_aggregate")
    op.drop_table("report_item_cpe")
    op.drop_table("report_item_attribute")
    op.drop_table("product_report_item")
    op.drop_table("news_item_vote")
    op.drop_table("asset_vulnerability")
    op.drop_table("asset_cpe")
    op.drop_table("user_role")
    op.drop_table("user_permission")
    op.drop_table("report_item")
    op.drop_table("publisher_preset_parameter_value")
    op.drop_table("product_type_parameter_value")
    op.drop_table("product")
    op.drop_table("news_item_data_news_item_attribute")
    op.drop_table("news_item_aggregate_news_item_attribute")
    op.drop_table("news_item")
    op.drop_table("asset")
    op.drop_table("acl_entry_user")
    op.drop_table("user")
    op.drop_table("remote_access_osint_source")
    op.drop_table("publisher_preset")
    op.drop_table("publisher_parameter")
    op.drop_table("product_type")
    op.drop_table("presenter_parameter")
    op.drop_table("osint_source_word_list")
    op.drop_table("osint_source_parameter_value")
    op.drop_table("osint_source_group_osint_source")
    op.drop_table("news_item_tag")
    op.drop_table("news_item_data")
    op.drop_table("news_item_attribute")
    op.drop_table("news_item_aggregate_search_index")
    op.drop_table("bot_parameter_value")
    op.drop_table("attribute_group_item")
    op.drop_table("asset_group")
    op.drop_table("word_list_entry")
    op.drop_table("role_permission")
    op.drop_table("remote_node")
    op.drop_table("remote_access_report_item_type")
    op.drop_table("publisher")
    op.drop_table("presenter")
    op.drop_table("parameter_value")
    op.drop_table("osint_source")
    op.drop_table("organization")
    op.drop_table("news_item_aggregate")
    op.drop_table("hotkey")
    op.drop_table("collector_parameter")
    op.drop_table("attribute_group")
    op.drop_table("attribute_enum")
    op.drop_table("acl_entry_role")
    op.drop_table("word_list")
    op.drop_table("user_profile")
    op.drop_table("token_blacklist")
    op.drop_table("tag_cloud")
    op.drop_table("role")
    op.drop_table("report_item_type")
    op.drop_table("remote_access")
    op.drop_table("publishers_node")
    op.drop_table("presenters_node")
    op.drop_table("permission")
    op.drop_table("parameter")
    op.drop_table("osint_source_group")
    op.drop_table("collectors_node")
    op.drop_table("collector")
    op.drop_table("bots_node")
    op.drop_table("bot")
    op.drop_table("attribute")
    op.drop_table("address")
    op.drop_table("acl_entry")
    # ### end Alembic commands ###