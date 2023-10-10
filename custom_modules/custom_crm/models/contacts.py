from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'


    raisonS = fields.Char(string="Raison sociale")
    juridique = fields.Many2one('forme.juridique', string="Forme juridique")
    responsable = fields.Char( string="Premier responsable")
    civilite = fields.Many2one('res.partner.title', string='Civilité du promoteur')
    secteur = fields.Many2one('res.partner.industry')
    email1 = fields.Char(string="Email de siège")
    email2 = fields.Char(string = "Email d\'usine")
    phone2 = fields.Char(string = "Téléphone usine", widget='phone')
    phone1 = fields.Char(string="Téléphone siège " , widget='phone')
    mobile1 = fields.Char(string ="Mobile siège", widget='phone')
    mobile2 = fields.Char(string="Mobile usine", widget='phone')
    fax2 = fields.Char(string="Fax usine",widget='phone',)
    fax1 = fields.Char(string="Fax siège", widget='phone')
    regime = fields.Selection([('exportatrice', 'Totalement exportatrice'),
                               ('non exportatrice ', 'Non Totalement exportatrice')], string="Régime")
    code = fields.Char(string="Code TVA")

    participant = fields.Char( string='Pays du participant étranger')
    date = fields.Char(string=" Date entrée en production")
    capital = fields.Integer(string="Capital social en DT" )
    emploi = fields.Integer(string="Emploi")

    street_seige = fields.Char(string="Adresse siège")
    street_usine = fields.Char(string="Adresse usine")
    name_city = fields.Many2one('delegation', string="Délégation d\'usine",
                                domain="[('state_id', '=?', state_id_usine)]")
    name_city_seige = fields.Many2one('delegation', string="Délégation du siège",
                                      domain="[('state_id', '=?', state_id_seige)]")

    state_id_usine = fields.Many2one("res.country.state", string="Gouvernorat d\'usine", ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")

    country_id_siege = fields.Many2one('res.country', string='Pays', ondelete='restrict')

    state_id_seige = fields.Many2one("res.country.state", string="Gouvernorat du siège", ondelete='restrict',
                                     domain="[('country_id', '=?', country_id_siege)]")
    zip_siege = fields.Char(string="code postal siège" ,change_default=True)
    zip_usine = fields.Char(string="code postal usine",change_default=True)

    is_industry = fields.Boolean()

    # to count the nomber of companies saved in contacts we will create a compute field
    # so we need the boolean field is_company to specify the company
    # saved company
    def get_default(self):
        return self.search_count([('is_industry', '=', True)])

    nb_company = fields.Integer(
        compute='_compute_total',
        default=get_default,  # Using the get_default function as the default value
        reverse=True
    )

    def _compute_total(self):
        for partner in self:
            partner.nb_company = self.search_count([('is_industry', '=', True)])


