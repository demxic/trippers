import pytest

from tripper.response_objects import response_objects as res


@pytest.fixture
def response_value():
    return {'key': ['value1', 'value2']}


@pytest.fixture
def response_type():
    return 'ResponseError'


@pytest.fixture
def response_message():
    return 'This is an error'


def test_response_success_is_true():
    assert bool(res.ResponseSuccess()) is True


def test_response_success_has_type_and_value(response_value):
    response = res.ResponseSuccess(response_value)

    assert response.type == res.ResponseSuccess.SUCCESS
    assert response.value == response_value

