from tripper.request_objects import airport_list_request_object as req


def test_build_airport_list_request_object_without_parameters():
    request = req.AirportListRequestObject()

    assert bool(request) is True


def test_build_airport_list_request_object_from_empty_dict():
    request = req.AirportListRequestObject.from_dict({})

    assert bool(request) is True
