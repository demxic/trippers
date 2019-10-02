# ------------- Version two with response and request objects:
import pytest
from unittest import mock

from tripper.domain.elements import Airport
from tripper.use_cases import airport_list_use_case as uc
from tripper.request_objects import airport_list_request_object as req


@pytest.fixture
def domain_airports():
    airport1 = Airport('MEX', 'America/Mexico_City')
    airport2 = Airport('GDL', 'America/Mexico_City')
    airport3 = Airport('JFK', 'America/NewYork_City')
    airport4 = Airport('MAD', 'Europe/Madrid')
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

# ------------- Version one without response and request objects:
#
# import pytest
# from unittest import mock
#
# from tripper.domain.elements import Airport
# from tripper.use_cases import airport_list_use_case as uc
#
#
# @pytest.fixture
# def domain_airports():
#     airport1 = Airport('MEX', 'America/Mexico_City')
#     airport2 = Airport('GDL', 'America/Mexico_City')
#     airport3 = Airport('JFK', 'America/NewYork_City')
#     airport4 = Airport('MAD', 'Europe/Madrid')
#     return [airport1, airport2, airport3, airport4]
#
#
# def test_airport_list_without_parameters(domain_airports):
#     repository = mock.Mock()
#     repository.list.return_value = domain_airports
#
#     airport_list_use_case = uc.AirportListUseCase(repository)
#     result = airport_list_use_case.execute()
#
#     repository.list.assert_called_with()
#     assert result == domain_airports
