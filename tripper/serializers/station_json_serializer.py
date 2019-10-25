import json


class StationJsonEncoder(json.JSONEncoder):

    def default(self, object):
        try:
            to_serialize = dict(
                __class__="Station",
                __args__=[],
                __kw__=dict(iata_code=object.iata_code,
                            zone=object.zone,
                            viaticum=object.viaticum
                            )
            )
            return to_serialize
        except AttributeError:
            return super().default(object)
