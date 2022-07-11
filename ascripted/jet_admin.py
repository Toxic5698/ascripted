# https://jet.readthedocs.io/en/latest/index.html

JET_SIDE_MENU_COMPACT = True

# JET_SIDE_MENU_ITEMS = [  # A list of application or custom item dicts
#     {'label': ('Client administration'), 'app_label': 'client', 'items': [
#         {'name': 'profile'},
#         {'name': 'worksheet', 'label': ('Work Sheets')},
#         {'name': 'payments', 'label': ('Payments')},
#         {'label': ('Analytics'), 'url': 'http://example.com', 'url_blank': True},
#     ]},
#     # {'label': _('Users'), 'items': [
#     #     {'name': 'core.user'},
#     #     {'name': 'auth.group'},
#     #     {'name': 'core.userprofile', 'permissions': ['core.user']},
#     # ]},
#     # {'app_label': 'banners', 'items': [
#     #     {'name': 'banner'},
#     #     {'name': 'bannertype'},
#     # ]},
# ]

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_INDEX_DASHBOARD = 'ascripted.dashboard.AscriptedDashboard'
