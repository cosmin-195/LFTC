# doc: regex, uml diagram, something else
import re
import symbolTable as sb


class Scanner:

    def __init__(self):
        self.operators = ['+', '-', '*', '/', '<', '<=', '=', '>=', 'eq', 'mod', 'not']
        self.keywords = ['init', 'verify', 'otherwise', 'escape', 'true', 'untrue', 'while', 'for', 'func', 'in']
        self.separators = [']', '[', '{', '}', ';', ' ']
        self.pif = []
        self.st = sb.SymbolTable()
        self.constSt = sb.SymbolTable()

    def __readFile(self):
        pass

    def scan(self, filename):
        with open('p1') as file:
            line = file.readline()
            line_nr = -1
            while line:
                line_nr += 1
                p1 = 0
                p2 = 0
                while p2 < len(line):
                    if line[p2] == ' ':
                        p2 += 1
                        p1 += 1
                        continue
                    if line[p2] in self.separators and line[p2] == '"':
                        # todo instead call regex:
                        #  if None ? exception : check start index to be same as p2 -> move p2 to end index
                        match = match_string(line[p2:])
                        if match is None:
                            # todo write to file
                            raise Exception('" is not matched - line' + str(line_nr))
                        else:
                            self.pif.append(("const", self.constSt.add(match.string)))

                line = file.readline()

    def __classify(self, token):
        pass


def special_split(line):
    first = line.find('"')


def match_int(s):
    return re.match("-*[1-9]+[0-9]*", s)


def match_identifier(s):
    return re.match("[a-zA-Z]+[a-zA-Z1-9_]*", s)


def match_string(s):
    return re.match('"[^\n"]*"', s)


st = ' fint = "vf d "'
f = st.find('"')
stb = sb.SymbolTable()
stb.add(re.match('"[^\n"]*"','"fd da d " 3f').string)

print(st.find('"',st.find('"',f+1)))
