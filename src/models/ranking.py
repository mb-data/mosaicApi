from . import db 

#configura modelo de dados do Lead
class Ranking(db.Model):
    __tablename__ = 'ranking'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255)) 
    phone = db.Column(db.String(255)) 
    points = db.Column(db.Integer)
    year = db.Column(db.Integer) 
    month = db.Column(db.Integer) 
  
    def __str__(self):
        return self.name

    def get_user_id(self):
        return self.id

  

