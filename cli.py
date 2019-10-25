from tripper.repository import memrepo as mr
from tripper.use_cases import station_list_use_case as uc

airport_data = [
        {'code': 'MEX', 'zone': 'America/Mexico_City', 'viaticum': None},
        {'code': 'GDL', 'zone': 'America/Mexico_City', 'viaticum': None},
        {'code': 'JFK', 'zone': 'America/New_York', 'viaticum': None},
        {'code': 'MAD', 'zone': 'Europe/Madrid', 'viaticum': None}
    ]

repo = mr.Memrepo(airport_data)
use_case = uc.AirportListUseCase(repo=repo)
result = use_case.execute()
print(result)