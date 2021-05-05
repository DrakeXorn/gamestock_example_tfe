{
    'name': 'Gamestock app',
    'summary': '',
    'version': '14.0.1.0.0',
    'depends': ['base'],
    'data': [
        # Data files
        'data/gamestock_genre.xml',
        'data/gamestock_editor.xml',

        # Views
        'views/gamestock_game_view.xml',
        
        # Security
        'security/ir.model.access.csv'
    ],
    'application': True
}