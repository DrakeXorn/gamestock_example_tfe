from odoo import models, fields, _


class GameEditor(models.Model):
    _name = 'gamestock.editor'
    _description = 'Gamestock game editor model'

    name = fields.Char('Name')
    creation_date = fields.Date('Creation date', default=fields.Date.today())
    game_ids = fields.One2many('gamestock.game', 'developer_id', 'Created games')


class GameGenre(models.Model):
    _name = 'gamestock.genre'
    _description = 'Gamestock game genre model'

    name = fields.Char('Game genre')
    first_release_date = fields.Date('First release date')
    game_ids = fields.One2many('gamestock.game', 'genre_id', 'Games targeted')


class Game(models.Model):
    _name = 'gamestock.game'
    _description = 'Gamestock game model'

    name = fields.Char('Game')
    release_date = fields.Date('Release date')
    description = fields.Text('Description')
    developer_id = fields.Many2one('gamestock.editor', 'Editor')
    genre_id = fields.Many2one('gamestock.genre', 'Game genre')
