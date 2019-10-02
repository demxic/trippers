class ResponseSuccess(object):

    def __init__(self, value=None):
        self.value = value

    def __bool__(self):
        return True
