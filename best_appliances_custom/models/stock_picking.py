# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    transportista_id = fields.Many2one(
        comodel_name='res.partner',
        string='Transportista'
    )
    licencia = fields.Char(string='Licencia')
    placa = fields.Char(string='Placa')
    inscripcion = fields.Char(string='Inscripcion')

    @api.onchange('transportista_id')
    def _onchange_transportista_id(self):
        self.licencia = False
        self.placa = False
        self.inscripcion = False
        if self.transportista_id:
            self.licencia = self.transportista_id.licencia
            self.placa = self.transportista_id.placa
            self.inscripcion = self.transportista_id.inscripcion