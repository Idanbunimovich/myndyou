from data_layer.lib.db import DB

class Base:
    def __init__(self, model):
       self.model = model

    def get_by_id(self, id):
        session = DB.session_factory()
        try:
            return session.filter(self.model.id == id).first()
        except:
            raise Exception("Request to sql failed")
        finally:
            session.close()


    def insert(self, items):
        session = DB.session_factory()
        try:
            for item in items:
                session.add(item)
            session.commit()
            for item in items:
                 session.refresh(item)
            return items
        except:
            session.rollback()
            raise Exception("Request to sql failed")
        finally:
            session.close()






