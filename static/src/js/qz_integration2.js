/** @odoo-module */
import { loadBundle } from "@web/core/assets";
var AbstractAction = require('web.AbstractAction');
var core = require('web.core');

if (typeof AbstractAction === 'undefined' || typeof core === 'undefined') {
    console.error("AbstractAction o core no están definidos. Asegúrate de que las dependencias estén cargadas correctamente.");
    return;
}

var PrintLabelAction = AbstractAction.extend({
    start: function () {
        var params = this.options.params;

        console.log('Printing label with product:', params.product_name, params.product_code);

        // Conectar a QZ Tray y enviar la etiqueta a la impresora
        QzTray.websocket.connect().then(function() {
            console.log("Connected to QZ Tray");

            var config = QzTray.configs.create("Zebra_Printer");
            var data = [
                {
                    type: 'raw',
                    format: 'file',
                    data: '^XA^FO50,50^A0N50,50^FD' + params.product_name + '^FS^FO50,120^FD' + params.product_code + '^FS^XZ'
                }
            ];

            // Enviar datos a la impresora
            QzTray.print(config, data).then(function() {
                console.log("Label printed successfully");
            }).catch(function(e) {
                console.error("Error printing label:", e);
            });

        }).catch(function(err) {
            console.error("Could not connect to QZ Tray:", err);
        });

        return this._super.apply(this, arguments);
    }
});

core.action_registry.add('print.label.qz', PrintLabelAction);