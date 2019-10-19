class InvalidRequestObject(object):

    def __init__(self):
        self.errors = []

    def add_error(self, parameter: str, message: str, airport_codes: list = None):
        self.errors.append({'parameter': parameter, 'message': message, 'airport_codes': airport_codes})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False


class ValidRequestObject(object):

    def __bool__(self):
        return True


class AirportListRequestObject(ValidRequestObject):
    accepted_code_length = 3

    def __init__(self, airport_codes: list = None):
        self.airport_codes = airport_codes

    @classmethod
    def from_airports_code_list(cls, airport_codes: list):
        invalid_req = InvalidRequestObject()

        if airport_codes:

            if not isinstance(airport_codes, list):
                invalid_req.add_error('airports_code_list', 'Is not iterable')
            elif len(airport_codes) == 0:
                invalid_req.add_error('airports_code_list', 'List is empty!')
            else:
                wrong_airport_codes = []
                for airport_code in airport_codes:
                    if (len(airport_code) != cls.accepted_code_length) or not airport_code.isalpha():
                        wrong_airport_codes.append(airport_code)
                if len(wrong_airport_codes) > 0:
                    invalid_req.add_error('airport_codes', 'Wrong airport codes!', wrong_airport_codes)

        if invalid_req.has_errors():
            return invalid_req

        return cls(airport_codes=airport_codes)
