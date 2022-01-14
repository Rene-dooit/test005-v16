# -*- coding: utf-8 -*-
# from odoo import http


# class SpecialPrice(http.Controller):
#     @http.route('/special_price/special_price', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/special_price/special_price/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('special_price.listing', {
#             'root': '/special_price/special_price',
#             'objects': http.request.env['special_price.special_price'].search([]),
#         })

#     @http.route('/special_price/special_price/objects/<model("special_price.special_price"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('special_price.object', {
#             'object': obj
#         })
