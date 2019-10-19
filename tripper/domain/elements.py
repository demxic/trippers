import datetime

import pytz


class Airport(object):

    def __init__(self, code: str, continent: str, tz_city: str, viaticum=None):
        self.code = code
        self.continent = continent
        self.tz_city = tz_city
        self.timezone = pytz.timezone(continent+'/'+tz_city)
        self.viaticum = viaticum

    def to_dict(self):
        return dict(iata_code=self.code, zone=self.timezone, viaticum=self.viaticum)

    def __eq__(self, other: 'Airport'):
        return self.to_dict() == other.to_dict()

    def __str__(self):
        return "{}".format(self.code)

    def __repr__(self):
        return "<Airport> {}".format(self.code)


class Location(object):
    """Airport where any event could happen

        It is itended to be used by any marker or ground duty that happen in one location.
    """

    def __init__(self, name: str, origin: Airport):
        self.name = name
        self.origin = origin
