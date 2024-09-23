from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import safe_eval
import html

class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = ['product.template','qz.tray']

    def print_label(self):
        self.zpl_code =html.unescape(f"^XA^CF0,30^FO30,30^A0N,20,20^FB360,3,,^FD{html.unescape(self.display_name)}^FS^FO90,100^BY2^BCN,60,,,A^FD12345678^FS^FO320,200^A0N,30,30^FD${self.list_price}^FS^FO460,30^A0N,20,20^FB360,3,,^FD{html.unescape(self.display_name)}^FS^FO490,100^BY2^BCN,60,,,A^FD12345678^FS^FO720,200^A0N,30,30^FD{self.list_price}^FS^XZ")
        res_id = '?res_id=%s&res_model=product.template'%(self.id)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': self.print_url + res_id,
        }
        
class StockLot(models.Model):
    _name = 'stock.lot'
    _inherit = ['stock.lot','qz.tray']

    def print_label(self):
        self.zpl_code =html.unescape(f"^XA^CF0,30^FO30,30^A0N,20,20^FB360,3,,^FD{html.unescape(self.display_name)}^FS^FO90,100^BY2^BCN,60,,,A^FD12345678^FS^FO320,200^A0N,30,30^FD${self.list_price}^FS^FO460,30^A0N,20,20^FB360,3,,^FD{html.unescape(self.display_name)}^FS^FO490,100^BY2^BCN,60,,,A^FD12345678^FS^FO720,200^A0N,30,30^FD{self.list_price}^FS^XZ")
        res_id = '?res_id=%s&res_model=product.template'%(self.id)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': self.print_url + res_id,
        }

class ZPLReport(models.Model):
    _name = 'zpl.report.template'
    zpl = fields.Text('ZPL')
    copies = fields.Integer('Copias',default=1)
    model_id = fields.Many2one('ir.model','Modelo')
    
    def update_zpl_field(self, zpl_text):
        self.write({'zpl': zpl_text})