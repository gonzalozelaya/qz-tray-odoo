from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval
import requests
import base64

class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = ['product.template','qz.tray']

    def print_label(self):
        self.zpl_code ='^XA^FDHola Mundo^XZ~PS'
        res_id = '?res_id=%s&res_model=product.template'%(self.id)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': self.print_url + res_id,
        }
