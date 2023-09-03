import pytest
from adapters import repository
from domain import model
from sqlalchemy.orm import Session
from sqlalchemy import text

pytestmark = pytest.mark.usefixtures("mappers")


def insert_data_with_more_fields(
        session: Session, data: model.DataWithMoreFields
) -> None:
    session.execute(
        text("INSERT INTO data_with_more_fields(first_string, second_integer)"
        "VALUES (:first_str, :second_int)"),
        dict(first_str=data.first_str, second_int=data.second_int)
    )


@pytest.fixture(autouse=True)
def db_teardown(postgres_session):
    yield
    postgres_session.query(model.MyData).delete()
    postgres_session.query(model.DataWithMoreFields).delete()
    postgres_session.commit()


def test_my_data_add_get_element(postgres_session):
    repo = repository.SqlALchemyReporitory(postgres_session)
    data = model.MyData(
        some_str="my text", some_float=3.14, some_int=5
    )
    repo.add(data)
    assert repo.get_last_my_data() == data
    assert postgres_session.query(model.MyData).count() == 1


def test_my_data_add_remove_element(postgres_session):
    repo = repository.SqlALchemyReporitory(postgres_session)
    data = model.MyData(
        some_str="my text2", some_float=3.14, some_int=5
    )

    repo.add(data)
    repo.delete(data)
    assert not repo.get_last_my_data()
    assert postgres_session.query(model.MyData).count() == 0


def test_data_with_more_fields_add_get_element(postgres_session):
    repo = repository.SqlALchemyReporitory(postgres_session)
    data = model.DataWithMoreFields(
        first_str="1st string", first_float=5.54, first_int=7,
        second_str="2nd string", second_int=9
    )

    repo.add(data)
    assert repo.get_last_data_with_more_fields() == data
    assert postgres_session.query(model.DataWithMoreFields).count() == 1


def test_data_with_more_fields_get(postgres_session_factory):
    session = postgres_session_factory()
    insert_data_with_more_fields(
        session,
        model.DataWithMoreFields(
            first_str="1st string", first_float=5.54, first_int=7,
            second_str="2nd string", second_int=9
        )
    )
    session.commit()
    session.close()
    repo = repository.SqlALchemyReporitory(postgres_session_factory())

    ret = repo.get_last_data_with_more_fields()
    assert ret == model.DataWithMoreFields(
            first_str="1st string", second_int=9
        )
