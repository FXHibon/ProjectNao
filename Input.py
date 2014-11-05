__author__ = 'fx'


class Input:
    "Represents input data for Nao, parsed from an input file"

    # Constructor
    def __init__(self, fileName):
        super().__init__()
        try:
            inputFile = open(fileName, 'r')
            self.grid = []
            for line in inputFile:
                self.grid += list(line).remove("\n")
            inputFile.close()
            print(self.grid)
        except FileNotFoundError as e:
            print("Cannot find " + fileName)

    def getNaoLocation(self):
        for line in self.grid:
            if "N" in line:
                return (line.index("N"), self.grid.index(line))
        return None