# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    l10n_pe_withhold_code = fields.Selection(selection_add=[('027', 'Servicio de transporte de bienes'), ('026',)])
