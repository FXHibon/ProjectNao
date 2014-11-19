__author__ = 'kirolloszaky'


class Nao:

    def __init__(self, grid, location):
        self.grid = grid
        self.location = location
        self.neurons = Neurons()

    def getLocation(self):
        self.location

    def start(self):
        self.neurons.start()
