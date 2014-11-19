from twisted.protocols.ftp import FileNotFoundError
from model.Case import Case

__author__ = 'fx'


class Grid:
    """
    Represents input data for Nao, parsed from an input file
    """

    # Constructor
    def __init__(self, fileName):
        super().__init__()
        try:
            inputFile = open(fileName, 'r')
            self.grid = []
            line = inputFile.readline()

            y = 0
            while line != "":
                tmp = []
                for char in line:
                    if char != "\n":
                        tmp.append(Case(char, (line.index(char), y)))
                self.grid.append(tmp)
                line = inputFile.readline()
                y += 1

            inputFile.close()
        except FileNotFoundError as e:
            print("Cannot find " + fileName)

    def getNaoLocation(self):
        for line in self.grid:
            for case in line:
                if case.isNao():
                    return case.getLocation()

    def showData(self):
        for line in self.grid:
            print(line)

    def getSize(self):
        return (len(self.grid), len(self.grid[0]))