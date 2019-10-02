import json

from tripper.domain.elements import Airport
from tripper.serializers import airport_json_serializer as ser


def test_serialize_domain_airport():
    airport = Airport(iata_code='MEX', zone='America/Mexico_City', viaticum=None)
    expected_json = '{"__class__": "Airport", "__args__": [], "__kw__": {"iata_code": "MEX", "zone": ' \
                    '"America/Mexico_City", "viaticum": null}} '

    json_airport = json.dumps(airport, cls=ser.AirportJsonEncoder)
    assert json.loads(json_airport) == json.loads(expected_json)
