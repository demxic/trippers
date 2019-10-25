from tripper.domain.elements import Station, Location


def test_location_init():
    mex_airport = Station(code='MEX', zone='America/Mexico_City', viaticum=None)
    location = Location(name='E2', origin=mex_airport)
    assert location.name == 'E2'
    assert location.origin == mex_airport
