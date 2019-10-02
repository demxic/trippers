import json


class AirportJsonEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'iata_code': o.iata_code,
                'zone': o.zone,
                'viaticum': o.viaticum
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
