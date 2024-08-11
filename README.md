# Test to Odoo developer
This repository contains a module that:
* Add a smart button in the model `product.template` that show the sale quantity of this product
* Create a wizard that allow to select many products and assign them a tag
* Create a model called `product.label`
## Getting started
### How to clone
```
f:\odoo\odoo\projects
$ git clone https://github.com/Mcfreestyle/test_odoo17
```
### How to install this module
1. Add the repository path in the odoo.conf
```
addons_path = f:\\odoo\odoo\addons, f:\\odoo\odoo\projects\test_odoo17
```
2. Create a database and run odoo
```
f:\odoo\odoo
$ python odoo-bin -d test_db
```
3. Install the module `product_sale`
## Version
Odoo 17 Community
## Author
* Michael Chambilla
