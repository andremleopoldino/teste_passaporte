from odoo.tests.common import TransactionCase
import re


class ContatosExtensaoTestCase(TransactionCase):
    def test_custom_field_integration(self):
            model_test = self.env['res.partner']
            model_test_data = {
                'name': 'André Leopoldino',
                'name_document_holder': 'André Leopoldino',
                'passport_number': 'AB1234567',

            }
            partner = model_test.create(model_test_data)
            if partner.passport_number and not re.match(r'^[A-Z]{2}\d{7}$', partner.passport_number):
                print('Formato invalido')
            else:
                print('Formato valido')
