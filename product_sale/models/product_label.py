# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductLabel(models.Model):
    _name = "product.label"

    name = fields.Char(
        string="Name")
    description = fields.Text(
        name="Description")
