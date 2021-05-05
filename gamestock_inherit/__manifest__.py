{
    'name': 'Gamestock app inherit',
    'summary': 'Inherited data from Gamestock',
    'version': '14.0.1.0.0',
    'depends': ['gamestock'],
    'data': [
        # Data files

        # Views
        'views/gamestock_inherit_game_view.xml',

        # Security
        'security/ir.model.access.csv',
    ],
    'application': True
}