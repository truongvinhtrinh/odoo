{
    'name': 'Trinh Base import',
    'description': """
1. Remove the button Import (temporary solution, better to have it only for Administrator / Settings
""",
    'category': 'Uncategorized',
    'depends': ['base_import'],
    'installable': True,
    'auto_install': False,
    'data': [
    ],
    'qweb': ['static/src/xml/import.xml'],
}
