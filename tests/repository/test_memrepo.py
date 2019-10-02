import pytest

from tripper.domain.elements import Airport
from tripper.repository import memrepo


@pytest.fixture
def airport_dicts():
    return [
        {'iata_code': 'MEX', 'zone': 'America/Mexico_City', 'viaticum': None},
        {'iata_code': 'GDL', 'zone': 'America/Mexico_City', 'viaticum': None},
        {'iata_code': 'JFK', 'zone': 'America/New_York', 'viaticum': None},
        {'iata_code': 'MAD', 'zone': 'Europe/Madrid', 'viaticum': None}
    ]


def test_repository_list_without_parameters(airport_dicts):
    repo = memrepo.Memrepo(airport_dicts)

    airports = [Airport(**a) for a in airport_dicts]
    assert repo.list() == airports
