from tripper.domain.elements import Airport, Location


def test_location_init():
    mex_airport = Airport(code='MEX', zone='America/Mexico_City', viaticum=None)
    location = Location(name='E2', origin=mex_airport)
    assert location.name == 'E2'
    assert location.origin == mex_airport
