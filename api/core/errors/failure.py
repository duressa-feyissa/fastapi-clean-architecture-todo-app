from core.common.equatable import Equatable

class Failure(Equatable):
    def __init__(self, properties=None):
        self.properties = properties or []

class ServerFailure(Failure):
    pass

class CacheFailure(Failure):
    pass
