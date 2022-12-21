# lr0

class Grammar:

    def __init__(self):
        self.N = []  # nonterminals
        self.E = []  # terminals
        self.P = {}  # productionz
        self.S = None  # start symbol
        self.contextFree = True

    def read_from_file(self, filename):
        with open(filename) as f:
            self.N = f.readline().split()
            self.E = f.readline().split()
            self.S = f.readline().strip()
            line = f.readline().strip()
            while line:
                split = line.split("->")
                left = split[0].strip()
                right = split[1].strip().split("|")
                for i in range(len(right)):
                    right[i] = right[i].strip()
                if left in self.P:
                    self.P[left] += right
                else:
                    self.P[left] = [] + right
                line = f.readline()

    def isCFG(self):
        for key in self.P:
            if (len(key)) > 1:
                return False
        return True


g = Grammar()
g.read_from_file("exampleCFG")
print(g.P)
