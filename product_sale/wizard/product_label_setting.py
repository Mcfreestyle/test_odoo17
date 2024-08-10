# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductLabelSetting(models.TransientModel):
    _name = "product.label.setting"

    product_ids = fields.Many2many(
        string="Products",
        comodel_name="product.template")

    label_ids = fields.Many2many(
        string="Labels",
        comodel_name="product.label")
