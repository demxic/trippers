from tripper.domain.elements import Airport


def test_airport_model_init():
    a = Airport(iata_code='MEX', zone='America/Mexico_City', viaticum=None)
    assert a.iata_code == 'MEX'
    assert a.zone == 'America/Mexico_City'
    assert a.viaticum is None


def test_airport_model_from_dict():
    airport_dict = {'iata_code': 'MEX', 'zone': 'America/Mexico_City', 'viaticum': None}
    a = Airport(**airport_dict)
    assert a.iata_code == 'MEX'
    assert a.zone == 'America/Mexico_City'
    assert a.viaticum is None


def test_airport_model_to_dict():
    airport_dict = {'iata_code': 'MEX', 'zone': 'America/Mexico_City', 'viaticum': None}
    a = Airport(**airport_dict)
    assert a.to_dict()


def test_airport_model_str():
    a = Airport(iata_code='MEX', zone='America/Mexico_City', viaticum=None)
    expected_result = 'MEX'
    assert str(a) == expected_result


def test_airport_model_repr():
    a = Airport(iata_code='MEX', zone='America/Mexico_City', viaticum=None)
    expected_result = '<Airport> MEX'
    assert repr(a) == expected_result


def test_airport_model_comparison():
    airport_dict = {'iata_code': 'MEX', 'zone': 'America/Mexico_City', 'viaticum': None}
    airport1 = Airport(**airport_dict)
    airport2 = Airport(**airport_dict)
    assert airport1 == airport2
