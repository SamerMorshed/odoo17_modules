from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'ToDo Task'

    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?', default=False)
    date = fields.Date('Date', required=True, default=fields.Date.context_today)
    user_id = fields.Many2one('res.users', 'User', default=lambda self: self.env.user, required=True)