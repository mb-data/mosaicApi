from flask_restplus import fields
from src.config.restplus import api


lead_request = api.model('Lead Request', {
    'name': fields.String(required=True, description='name') ,
    'email': fields.String(required=True, description='email'),
    'phone': fields.String(required=True, description='phone'),
    'insta': fields.String(required=True, description='insta') 
})

lead_result = api.model('Lead Result', {
    'id': fields.Integer(required=True, description='Post Id'),
    'name': fields.String(required=True, description='lead_name') ,
    'email': fields.String(required=True, description='email'),
    'phone': fields.String(required=True, description='phone'),
    'insta': fields.String(required=True, description='insta')
})
