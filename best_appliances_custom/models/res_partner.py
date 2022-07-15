# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    licencia = fields.Char(string='Licencia')
    placa = fields.Char(string='Placa')
    inscripcion = fields.Char(string='Inscripcion')
