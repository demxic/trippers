import json

from tripper.domain.elements import Station
from tripper.serializers import station_json_serializer as ser


def test_serialize_domain_station():
    station = Station(code='MEX', zone='America/Mexico_City', viaticum=None)
    expected_json = '{"__class__": "Station", "__args__": [], "__kw__": {"code": "MEX", "zone": ' \
                    '"America/Mexico_City", "viaticum": null}} '

    json_station = json.dumps(station, cls=ser.stationJsonEncoder)
    assert json.loads(json_station) == json.loads(expected_json)
