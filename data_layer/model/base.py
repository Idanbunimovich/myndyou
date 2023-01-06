from data_layer.lib.db import DB
from sqlalchemy import and_

class Base:
    def __init__(self, model):
       self.model = model

    @DB.append_session
    def get(self, filter_arr, session):
        query = session.query(self.model)
        if len(filter_arr):
            query = query.filter(and_(*filter_arr))
        return query.first()
        session.close()

    @DB.append_session
    def insert(self, items, session):
        for item in items:
            session.add(item)
        session.commit()






