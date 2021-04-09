from django.apps import AppConfig


class ModuleConfig(AppConfig):
    name = 'test_plugin'
    version = '0.1'
    EXCLUDED_PERMISSIONS_MODELS = ['testmodel1',]
    EXCLUDED_PERMISSIONS_CODENAMES = ['add_testmodel2',]
    RENAMING_MODELS_NAMES = {
        'testmodel2': 'Testing Model 2',
    }
    MENU_SUBITEMS = {
        "dashboard": [
            {
                "name": "Dashboard subitem",
                "url_name": "dashboard-subitem"
            },
            {
                "name": "Dashboard subitem2",
                "url_name": "dashboard-subitem"
            }
        ],
        "users": [
            {
                "name": "Users subitem",
                "url_name": "users-subitem"
            },
            {
                "name": "Users subitem2",
                "url_name": "users-subitem"
            }
        ]
    }
    CREATE_ITEMS = [
        {
            "name": "create test",
            "url_name": "users-subitem"
        }
    ]
