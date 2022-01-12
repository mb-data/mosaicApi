from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.ranking_serializer import ranking_result, ranking_request
from src.services.ranking_service import create, getall
 

ns = api.namespace('api/ranking', description='Operations related to lead')

 
@ns.route('')
class RankingCollection(Resource):
    @api.expect(ranking_request)
    @api.marshal_with(ranking_result)
    def post(self):
        """
        Create a new Lead
        """ 
        ranking = create(request.json)
        return ranking 

    @api.marshal_with(ranking_result)#define resultado da metodo 
    def get(self):
        ranking_list = getall()
        return ranking_list
 

