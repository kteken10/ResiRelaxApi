from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User():
    def init__(self,firstName,lastName,id):
        self.id=id
        self.firstName=firstName
        self.lastName=lastName
        return self
    def __repr__(self):
        print(f" {self.firstName}")    

class Client(db.model):
    pass
class Reservation(db.model):
    pass
class Chambre(db.model):
    pass
class Paiement(db.model):
    pass
class Employer_Hotel(db.model):
    pass
class Service_hotel(db.model):
    pass
class User_service(db.model):
    pass


 


    