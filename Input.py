__author__ = 'fx'


class Input:
    "Represents input data for Nao, parsed from an input file"

    # Constructor
    def __init__(self, fileName):
        super().__init__()
        try:
            inputFile = open(fileName, 'r')
            self.grid = list()
            for line in inputFile:
                print(line)
                self.grid.append(list(line).remove("\n"))
            inputFile.close()
            print(self.grid)
        except:
            print("Error in file parsing")



    def getNaoLocation(self):
        for line in self.grid:
            if "N" in line:
                return ()
