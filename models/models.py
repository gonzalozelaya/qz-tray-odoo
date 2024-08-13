from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval
import requests
import base64

class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = ['product.template','qz.tray']

    def print_label(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.client',
            'tag': 'print.label.qz',
            'params': {
                'product_name': self.name,
                'product_code': self.default_code,
            },
        }
       

