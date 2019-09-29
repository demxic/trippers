class Airport(object):

    def __init__(self, iata_code: str, zone: str, viaticum=None):
        self.iata_code = iata_code
        self.zone = zone
        self.viaticum = viaticum

    def to_dict(self):
        return dict(iata_code=self.iata_code, zone=self.zone, viaticum=self.viaticum)

    def __str__(self):
        return "{}".format(self.iata_code)

    def __repr__(self):
        return "<Airport> {}".format(self.iata_code)
