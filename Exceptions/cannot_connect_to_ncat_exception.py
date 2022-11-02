class CannotConnectToNCATException(Exception):
    def __init__(self, reason):
        message = 'Cannot connect to NCAT: ' + reason
        super().__init__(message)
