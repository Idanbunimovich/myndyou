from data_layer.lib.db import DB
from sqlalchemy import and_

class Base:
    def __init__(self, model):
       self.model = model

    def get(self, filter_arr):
        session = DB.session_factory()
        try:
            query = session.query(self.model)
            if len(filter_arr):
                query = query.filter(and_(*filter_arr))
                return query.first()
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






