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