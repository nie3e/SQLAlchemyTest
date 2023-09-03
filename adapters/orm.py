from sqlalchemy import Table, MetaData, Column, Integer, String, Float, \
    PrimaryKeyConstraint
from sqlalchemy.orm import registry

from domain import model

mapper_registry = registry()

my_data = Table(
    "my_data", mapper_registry.metadata,
    Column("some_str", String),
    Column("some_float", Float),
    Column("some_int", Integer),
    PrimaryKeyConstraint("some_str", "some_float", "some_int")
)

data_with_more_fields = Table(
    "data_with_more_fields", mapper_registry.metadata,
    Column("first_string", String),
    Column("second_integer", Integer),
    PrimaryKeyConstraint("first_string", "second_integer")
)


def start_mappers():
    mapper_registry.map_imperatively(model.MyData, my_data)

    mapper_registry.map_imperatively(
        model.DataWithMoreFields, data_with_more_fields, properties={
            "first_str": data_with_more_fields.c.first_string,
            "second_int": data_with_more_fields.c.second_integer,
        }
    )
