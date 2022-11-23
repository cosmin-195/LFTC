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
            self.S = f.readline()
            line = f.readline()
            while line:
                split = line.split("->")
                left = line[0].strip()
                right = line[1].strip().split("|")
                if left in self.P:
                    state = self.P[left]
                    # self.P[[]]
                    self.contextFree = False
                else:
                    self.P[left] = right
                line = f.readline()
