# -*- coding: utf-8 -*-

from num2words import num2words

from odoo import models


class ResCurrency(models.Model):
    _inherit = "res.currency"

    def l10n_pe_edi_amount_to_text(self, amount_total):
        self.ensure_one()
        amount_i, amount_d = divmod(amount_total, 1)
        amount_d = int(round(amount_d * 100, 2))
        words = num2words(amount_i, lang='es')
        result = '%(words)s Y %(amount_d)02d/100 %(currency_name)s' % {
            'words': words,
            'amount_d': amount_d,
            'currency_name': self.currency_unit_label,
        }
        return result.upper()
