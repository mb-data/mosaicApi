from src.models import db
from src.models.lead import Lead
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
 
        lead = Lead(name=name,email=email, phone=phone)
        db.session.add(lead)
        db.session.commit()

        return lead

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        lead = Lead.query.filter_by(id=id).first()

        if not lead:
            json_abort(400,"Lead not found")
        else:
            return lead

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def getall():
    try:
        lead = Lead.query.all()

        if not lead:
            json_abort(400,"Lead not found")
        else:
            return lead

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

