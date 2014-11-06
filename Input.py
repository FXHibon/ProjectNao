__author__ = 'fx'


class Input:
    "Represents input data for Nao, parsed from an input file"

    # Constructor
    def __init__(self, fileName):
        super().__init__()
        try:
            inputFile = open(fileName, 'r')
            self.grid = []
            line = inputFile.readline()

            while line != "":
                tmp = list(line)[0:-1]
                print(len(tmp))
                if len(tmp) > 0:
                    self.grid.append(tmp)
                line = inputFile.readline()

            inputFile.close()
        except FileNotFoundError as e:
            print("Cannot find " + fileName)

    def getNaoLocation(self):
        for iLine in range(len(self.grid)):
            for iCol in range(len(self.grid[iLine])):
                if self.grid[iLine][iCol] == "N":
                    return (iLine, iCol)
        return None

    def getData(self):
        for line in self.grid:
            print(line)

    def getSize(self):
        return (len(self.grid), len(self.grid[0]))