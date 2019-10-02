import json

from domain.elements import Airport
from serializers import airport_json_serializer as ser


def test_serialize_domain_airport():
    airport = Airport(iata_code='MEX', zone='America/Mexico_City', viaticum=None)
    expected_json = """
        {
            "iata_code": "MEX",
            "zone": "America/Mexico_City",
            "viaticum": null
        }
    """

    json_airport = json.dumps(airport, cls=ser.AirportJsonEncoder)
    assert json.loads(json_airport) == json.loads(expected_json)