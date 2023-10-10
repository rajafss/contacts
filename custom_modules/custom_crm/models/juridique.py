from odoo import models, fields


class CustomCRMLead(models.Model):
    _name = 'forme.juridique'


    name = fields.Char(string="forme juridique")