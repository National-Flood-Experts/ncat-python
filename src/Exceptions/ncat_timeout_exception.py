class NCATTimeoutException(Exception):
    def __init__(self):
        message = 'The connection to the NCAT server has timed out'
        super().__init__(message)
