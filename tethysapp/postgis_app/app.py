from tethys_sdk.base import TethysAppBase
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting


class PostgisApp(TethysAppBase):
    """
    Tethys app class for PostGIS App.
    """

    name = 'PostGIS App'
    description = ''
    package = 'postgis_app'
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'postgis-app'
    color = '#e74c3c'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def persistent_store_settings(self):
        ps_settings = (
            PersistentStoreDatabaseSetting(
                name='flooded_addresses',
                description='PostGIS database',
                initializer='postgis_app.model.init_flooded_addresses_db',
                spatial=True,
                required=True
            ),
        )

        return ps_settings
