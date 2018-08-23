# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CausalePagamento(models.Model):
    _name = 'causale.pagamento'
    _description = 'Causale Pagamento'

    @api.constrains('code')
    def _check_code(self):
        domain = [('code', '=', self.code)]
        elements = self.search(domain)
        if len(elements) > 1:
            raise ValidationError(
                _("The element with code %s already exists") % self.code)

    @api.multi
    def name_get(self):
        res = []
        for cau in self:
            name = "%s - %s" % (cau.code, cau.name)
            if len(name) > 50:
                name = name[:50] + '...'
            res.append((cau.id, name))
        return res

    code = fields.Char(string='Code', size=2, required=True)
    name = fields.Char(string='Description', required=True)
