# ----------- Version 2 with response and request objects
from tripper.response_objects import response_objects as res


class AirportListUseCase(object):

    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        airports = self.repo.list()
        return res.ResponseSuccess(airports)


# ----------- Version 1 without response and request objects
# class AirportListUseCase(object):
#
#     def __init__(self, repo):
#         self.repo = repo
#
#     def execute(self):
#         return self.repo.list()
