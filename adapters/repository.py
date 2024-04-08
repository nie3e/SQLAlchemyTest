from typing import Union

from domain import model


class SqlAlchemyRepository:
    def __init__(self, session):
        self.session = session

    def add(self, my_data: Union[model.MyData, model.DataWithMoreFields]):
        self.session.add(my_data)
        self.session.commit()

    def get_my_data_by_oid(self, oid: int):
        return self.session.query(model.MyData).filter_by(oid=oid).first()

    def get_last_my_data(self):
        return self.session.query(model.MyData).first()

    def delete(self, my_data: Union[model.MyData, model.DataWithMoreFields]):
        self.session.delete(my_data)
        self.session.commit()

    def get_last_data_with_more_fields(self):
        return self.session.query(model.DataWithMoreFields).first()
