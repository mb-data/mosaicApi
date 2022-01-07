from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.lead_serializer import lead_result, lead_request
from src.services.lead_service import create, get, getall
 

ns = api.namespace('api/lead', description='Operations related to lead')

 
@ns.route('')
class LeadCollection(Resource):
    @api.expect(lead_request)
    @api.marshal_with(lead_result)
    def post(self):
        """
        Create a new Lead
        """ 
        lead = create(request.json)
        return lead 

    @api.marshal_with(lead_result)#define resultado da metodo 
    def get(self):
        lead_list = getall()
        return lead_list
 

@ns.route('/<int:id>')
class AuthorIDCollection(Resource): 
    @api.marshal_with(lead_result)
    def get(self, id):
        """
        Get lead by ID
        """ 
        lead = get(id)
        return lead 