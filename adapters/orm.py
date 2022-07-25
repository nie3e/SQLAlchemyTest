from sqlalchemy import Table, MetaData, Column, Integer, String, Float, \
    PrimaryKeyConstraint
from sqlalchemy.orm import mapper

from domain import model

metadata = MetaData()

my_data = Table(
    "my_data", metadata,
    Column("some_str", String),
    Column("some_float", Float),
    Column("some_int", Integer),
    PrimaryKeyConstraint("some_str", "some_float", "some_int"),
    postgresql_with_oids=True,
)

data_with_more_fields = Table(
    "data_with_more_fields", metadata,
    Column("first_string", String),
    Column("second_integer", Integer),
    PrimaryKeyConstraint("first_string", "second_integer"),
    postresql_with_oids=True,
)


def start_mappers():
    mapper(model.MyData, my_data)

    mapper(model.DataWithMoreFields, data_with_more_fields, properties={
        "first_str": data_with_more_fields.c.first_string,
        "second_int": data_with_more_fields.c.second_integer,
    })
