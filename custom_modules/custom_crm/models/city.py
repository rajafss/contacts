from odoo import models, fields


class City(models.Model):
    _name = 'delegation'
    _rec_name = 'name_city'


    name_city = fields.Char(string = "Délégation")
    state_id = fields.Many2one('res.country.state',string="Gouvernorat")