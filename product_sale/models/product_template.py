# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_sale_count = fields.Integer(
        string="Sale Count",
        compute="_compute_product_sale_count")

    def _compute_product_sale_count(self):
        for record in self:
            record.product_sale_count = self.env["sale.order.line"].search_count([
                ("product_template_id", "=", record.id)
            ])

    def action_open_sales(self):
        self.ensure_one()
        return {
            "name": "Sales",
            "type": "ir.actions.act_window",
            "res_model": "sale.order",
            "view_mode": "tree,form",
            # "domain": [
            # ]
        }
