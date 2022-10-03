class RequiredParameterMissingException(Exception):
    def __init__(self, parameter):
        message = 'Missing required parameter: ' + parameter
        super().__init__(message)
