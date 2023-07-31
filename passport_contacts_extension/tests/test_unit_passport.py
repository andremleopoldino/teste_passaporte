from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestCase(TransactionCase):

    def setUp(self):
            super(TestCase, self).setUp()
            self.partner_model = self.env['res.partner']

    def test_create_partner(self):
            data = {
                'name': 'André Leopoldino',
                'name_document_holder': 'name_document_holder',
                

            }
            partner = self.partner_model.create(data)
            self.assertEqual(partner.name_document_holder, 'name_document_holder', "Nome completo não está correto.")
            

