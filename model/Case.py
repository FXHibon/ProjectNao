__author__ = 'fx'


class Case:
    """
    Represents a single case
    """

    def __init__(self, type, location):
        self.type = type
        self.discovered = False
        self.location = location

    def isEmpty(self):
        return self.type == "0"

    def isNao(self):
        return self.type == "N"

    def isObstacle(self):
        return self.type == "x"

    def isDiscovered(self):
        return self.discovered

    def getLocation(self):
        return self.location

    def __str__(self):
        return self.type

