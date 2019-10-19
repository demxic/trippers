import pytz
from tripper.domain.elements import Airport


def test_airport_model_init():
    a = Airport(code='MEX', continent='America', tz_city='Mexico_City', viaticum=None)
    assert a.code == 'MEX'
    assert a.continent == 'America'
    assert a.tz_city == 'Mexico_City'
    assert a.viaticum is None
    assert a.timezone == pytz.timezone('America/Mexico_City')


def test_airport_model_from_dict():
    airport_dict = {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
    a = Airport(**airport_dict)
    assert a.code == 'MEX'
    assert a.continent == 'America'
    assert a.tz_city == 'Mexico_City'
    assert a.viaticum is None
    assert a.timezone == pytz.timezone('America/Mexico_City')


def test_airport_model_to_dict():
    airport_dict = {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
    a = Airport(**airport_dict)
    assert a.to_dict()


def test_airport_model_str():
    a = Airport(code='MEX', continent='America', tz_city='Mexico_City', viaticum=None)
    expected_result = 'MEX'
    assert str(a) == expected_result


def test_airport_model_repr():
    a = Airport(code='MEX', continent='America', tz_city='Mexico_City', viaticum=None)
    expected_result = '<Airport> MEX'
    assert repr(a) == expected_result


def test_airport_model_comparison():
    airport_dict = {'code': 'MEX', 'continent': 'America', 'tz_city': 'Mexico_City', 'viaticum': None}
    airport1 = Airport(**airport_dict)
    airport2 = Airport(**airport_dict)
    assert airport1 == airport2
