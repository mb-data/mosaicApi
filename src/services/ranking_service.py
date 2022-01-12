from src.models import db
from src.models.ranking import Ranking
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError 

### LEAD SERVICE
### gerenciar as regras de negocio e CRUD do author
###

def create(data):
    try:

        name = data.get('name')
        if not name:
            json_abort(400,"First Name is required")

        email = data.get('email')
        if not email:
            json_abort(400,"email is required")

        phone = data.get('phone')
        if not email:
            json_abort(400,"phone is required")
 
        points = data.get('points')
        if not points:
            json_abort(400,"phone is required")

        year = data.get('year')
        if not year:
            json_abort(400,"phone is required")

        month = data.get('month')
        if not month:
            json_abort(400,"phone is required")

        ranking = Ranking(name=name,email=email, phone=phone)
        db.session.add(ranking)
        db.session.commit()

        return ranking

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)



def getall():
    try:
        ranking = Ranking.query.all()

        if not ranking:
            json_abort(400,"Ranking not found")
        else:
            return ranking

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

