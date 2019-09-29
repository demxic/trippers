from domain.elements import Airport


def test_airport_init():
    a = Airport(iata_code='MEX', zone='America/Mexico_City', viaticum=None)
    assert a.iata_code == 'MEX'
    assert a.zone == 'America/Mexico_City'
    assert a.viaticum is None


def test_airport_to_dict():
    d = {'iata_code': 'MEX', 'zone': 'America/Mexico_City', 'viaticum': None}
    a = Airport(**d)
    assert a.to_dict()


def test_airport_str():
    a = Airport(iata_code='MEX', zone='America/Mexico_City', viaticum=None)
    expected_result = 'MEX'
    assert str(a) == expected_result


def test_airport_repr():
    a = Airport(iata_code='MEX', zone='America/Mexico_City', viaticum=None)
    expected_result = '<Airport> MEX'
    assert repr(a) == expected_result
