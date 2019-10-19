
from tripper.request_objects import airport_list_request_object as req


def test_build_airport_list_request_object_without_parameters():
    request = req.AirportListRequestObject()

    assert request.airport_codes is None
    assert bool(request) is True


def test_build_airport_list_request_object_with_empty_list():
    request = req.AirportListRequestObject([])

    assert len(request.airport_codes) == 0
    assert bool(request) is True


def test_build_airport_list_request_object_with_rejected_codes():
    airport_codes = ['MEX', 'ACAP', 'GDL', 'MT', 'FCO', 'M4D', '679', 'AM$', 'T@M', 'T#&']
    request = req.AirportListRequestObject.from_airports_code_list(airport_codes= airport_codes)

    assert request.has_errors()
    assert request.errors[0]['parameter'] == 'airport_codes'
    assert request.errors[0]['airport_codes'] == ['ACAP', 'MT', 'M4D', '679', 'AM$', 'T@M', 'T#&']
    assert bool(request) is False


def test_build_airport_list_request_object_with_accepted_codes():
    airport_codes = ['MEX', 'ACA', 'GDL', 'MTY', 'FCO']
    request = req.AirportListRequestObject.from_airports_code_list(airport_codes=airport_codes)

    assert request.airport_codes == airport_codes
    assert bool(request) is True



