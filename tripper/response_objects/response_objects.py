class ResponseSuccess(object):

    def __init__(self, value=None, type=None):
        self.value = value
        self.type = "SUCCESS"

    def __bool__(self):
        return True
