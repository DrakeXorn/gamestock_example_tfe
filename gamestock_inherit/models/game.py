from odoo import models, fields


class GameFranchise(models.Model):
    _name = 'gamestock_inherit.franchise'
    _description = 'Gamestock game franchise model'

    name = fields.Char('Name')
    game_ids = fields.One2many('gamestock.game', 'franchise_id', 'Related games')


class GameInherit(models.Model):
    _inherit = 'gamestock.game'

    franchise_id = fields.Many2one('gamestock_inherit.franchise', 'Franchise')
