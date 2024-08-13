odoo.define('qz-tray-odoo.qz_integration',['@web/client_actions/action_service','@web/core/registry'], function (require) {
    'use strict';
    var AbstractAction = require('@web/client_actions/action_service');
    var core = require('@web/core/registry');

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

    core.category('actions').add('print.label.qz', PrintLabelAction);
});