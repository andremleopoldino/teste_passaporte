from odoo import api, fields, models, _,exceptions
from odoo.exceptions import MissingError, ValidationError, AccessError
import re

class ResPartner(models.Model):
    _inherit = 'res.partner'

    name_document_holder = fields.Char(string='Nome do titular do Passaporte')
    country_ids = fields.Many2one('res.country', string='País')
    passport_number = fields.Char(string='Número do Passaporte')
    emission_date = fields.Date()
    expiry_date = fields.Date()
    

    @api.constrains('passport_number')
    def _validate_passport_number(self):
        for records in self:
            if records.passport_number and not re.match(r'^[A-Z]{2}\d{7}$', records.passport_number):
                raise ValidationError('Invalid passport number format!')



    