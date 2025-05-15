# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task'
    _order = 'date_deadline'
    
    name = fields.Char('Task Name', required=True)
    description = fields.Text('Description')
    date_start = fields.Date(string='Start Date', required=True, default=fields.Date.today)
    date_deadline = fields.Date(string='Deadline', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete')
    ], string='Status', default='draft', tracking=True)
    tag_ids = fields.Many2many('todo.tag', string='Tags')
    participant_ids = fields.Many2many('res.users', string='Participants')
    color = fields.Integer('Color Index')
    is_done = fields.Boolean('Completed', default=False)
    
    @api.onchange('is_done')
    def _onchange_is_done(self):
        """Update state when is_done changes"""
        for record in self:
            if record.is_done and record.state != 'complete':
                record.state = 'complete'
            elif not record.is_done and record.state == 'complete':
                record.state = 'draft'

    @api.onchange('state')
    def _onchange_state(self):
        """Update is_done when state changes to complete"""
        for record in self:
            if record.state == 'complete':
                record.is_done = True
            elif record.state != 'complete':
                record.is_done = False

    @api.constrains('date_start', 'date_deadline')
    def _check_deadline_date(self):
        for record in self:
            if record.date_deadline and record.date_start and record.date_deadline < record.date_start:
                raise ValidationError(_("Deadline must be greater than or equal to Start Date."))
    
    @api.onchange('is_done')
    def _onchange_is_done(self):
        if self.is_done:
            self.state = 'complete'
        elif self.state == 'complete':
            self.state = 'in_progress'

class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Todo Tag'
    
    name = fields.Char('Tag Name', required=True)
    color = fields.Integer('Color Index')