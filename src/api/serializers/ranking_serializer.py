from flask_restplus import fields
from src.config.restplus import api


ranking_request = api.model('Ranking Request', {
    'name': fields.String(required=True, description='name') ,
    'email': fields.String(required=True, description='email'),
    'phone': fields.String(required=True, description='phone'), 
    'points': fields.Integer(required=True, description='pontis'), 
    'year': fields.Integer(required=True, description='year'),
    'month': fields.Integer(required=True, description='month')
})

ranking_result = api.model('Ranking Result', {
    'id': fields.Integer(required=True, description='Post Id'),
    'name': fields.String(required=True, description='lead_name') ,
    'email': fields.String(required=True, description='email'),
    'phone': fields.String(required=True, description='phone'), 
    'points': fields.Integer(required=True, description='pontis'), 
    'year': fields.Integer(required=True, description='year'),
    'month': fields.Integer(required=True, description='month')
})
