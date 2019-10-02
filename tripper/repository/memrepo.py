from tripper.domain.elements import Airport


class Memrepo(object):

    def __init__(self, data):
        self.data = data

    def list(self):
        return [Airport(**a) for a in self.data]