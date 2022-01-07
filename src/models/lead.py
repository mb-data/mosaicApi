from . import db 

#configura modelo de dados do Lead
class Lead(db.Model):
    __tablename__ = 'lead'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255)) 
    phone = db.Column(db.String(255)) 


    def __str__(self):
        return self.name

    def get_user_id(self):
        return self.id

  

