from tripper.repository import memrepo as mr
from tripper.use_cases import airport_list_use_case as uc

airport_data = [
        {'iata_code': 'MEX', 'zone': 'America/Mexico_City', 'viaticum': None},
        {'iata_code': 'GDL', 'zone': 'America/Mexico_City', 'viaticum': None},
        {'iata_code': 'JFK', 'zone': 'America/New_York', 'viaticum': None},
        {'iata_code': 'MAD', 'zone': 'Europe/Madrid', 'viaticum': None}
    ]

repo = mr.Memrepo(airport_data)
use_case = uc.AirportListUseCase(repo=repo)
result = use_case.execute()
print(result)