# ------------- Version two with response and request objects:
import pytest
from unittest import mock

import pytz

from tripper.domain.elements import Airport
from tripper.use_cases import airport_list_use_case as uc
from tripper.request_objects import airport_list_request_object as req


@pytest.fixture
def domain_airports():
    airport1 = Airport(code='MEX', timezone=pytz.timezone('America/Mexico_City'))
    airport2 = Airport(code='GDL', timezone=pytz.timezone('America/Mexico_City'))
    airport3 = Airport(code='JFK', timezone=pytz.timezone('America/New_York'))
    airport4 = Airport(code='MAD', timezone=pytz.timezone('Europe/Madrid'))
    return [airport1, airport2, airport3, airport4]


def test_airport_list_without_parameters(domain_airports):
    repository = mock.Mock()
    repository.list.return_value = domain_airports

    airport_list_use_case = uc.AirportListUseCase(repository)
    request = req.AirportListRequestObject()

    response = airport_list_use_case.execute(request)

    assert bool(response) is True
    repository.list.assert_called_with()
    assert response.value == domain_airports
