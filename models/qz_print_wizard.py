from odoo import api, fields, models

class QZPrintTemplate(models.TransientModel):
    _name = 'qz.print.wizard'
    _description = 'QZ Print Template Wizard'

    zpl_code = fields.Text(string='ZPL Code', required=True)
    copies_number = fields.Integer(string='Number of Copies', default=1, required=True)
    printer_name = fields.Char(string='Printer Name', default='ZDesigner', required=True)

    def action_print_label(self):
        """
        Acción que se ejecuta cuando se presiona el botón de imprimir.
        Aquí podrías integrar la lógica para enviar el ZPL a la impresora a través de QZ Tray.
        """
        # Ejemplo de código para mostrar valores en el log (puedes adaptar esto según tu lógica de impresión)
        self.ensure_one()
        print("ZPL Code:", self.zpl_code)
        print("Number of Copies:", self.copies_number)
        print("Printer Name:", self.printer_name)
        
        # Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}


zpl_report = env['zpl.report'].browse(1)
label_number = 1
zpl_code = ''
for rec in records:
    list_price_formatted = f"{rec.list_price:.2f}" 
    if label_number <= 1:
        zpl_code += '^XA'
        zpl_code += f"^CF0,30^FO30,30^A0N,20,20^FB360,3,,^FD{rec.display_name}^FS^FO60,100^BY2^BCN,60,,,A^FD{rec.barcode}^FS^FO320,200^A0N,30,30^FD${list_price_formatted}"
    else:
        zpl_code += f"^FS^FO460,30^A0N,20,20^FB360,3,,^FD{rec.display_name}^FS^FO480,100^BY2^BCN,60,,,A^FD{rec.barcode}^FS^FO720,200^A0N,30,30^FD{list_price_formatted}^FS^XZ"
        label_number = 0
    label_number +=1
if label_number >= 2:
    zpl_code += "^XZ"
    
res_id = '?res_id=%s&res_model=zpl.report'%(zpl_report.id)
zpl_code.replace('&nbsp;',' ')
zpl_report.write({'zpl_code':zpl_code})
action = {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': rec[0].print_url + res_id,
        }
