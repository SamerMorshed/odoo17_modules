from odoo import http

class TodoAppController(http.Controller):
    @http.route('/todo_app', auth='user', website=True)
    def todo_app(self):
        return http.request.render('todo_app.todo_app_page', {})