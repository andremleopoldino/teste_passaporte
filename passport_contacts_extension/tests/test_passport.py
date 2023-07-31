from odoo.tests.common import TransactionCase
import re


class ContatosExtensaoTestCase(TransactionCase):
    def test_custom_field_integration(self):
            model_test = self.env['res.partner']
            model_test_data = {
                'name': 'André Leopoldino',
                'nome_completo': 'André Leopoldino',
                'passport_number': 'AB123456',

            }
            partner = model_test.create(model_test_data)
            if partner.numero_do_passaporte and not re.match(r'^[A-Z]{2}\d{7}$', partner.numero_do_passaporte):
                print('Formato invalido')
            else:
                print('Formato valido')
