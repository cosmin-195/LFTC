# doc: regex, uml diagram, something else
import re
import symbolTable as sb
from enum import Enum

class Scanner:

    def __init__(self, file):
        self.file = file
        self.operators = ['+', '-', '*', '/', '<', '<=', '=', '>=', 'eq', 'mod', 'not']
        self.keywords = ['init', 'verify', 'otherwise', 'escape', 'true', 'untrue', 'while', 'for', 'func', 'in']
        self.separators = [']', '[', '{', '}', ';', ' ', '(', ")", ","]
        self.pif = []
        self.st = sb.SymbolTable()
        self.constSt = sb.SymbolTable()
        self.tokens = []

    def scan(self):
        self.__tokenize(self.file)
        for token in self.tokens:
            self.__classify(token)

    def __tokenize(self, filename):
        with open(filename) as file:
            line = file.readline()
            line_nr = -1
            while line:
                line_nr += 1
                p1 = 0
                p2 = 0
                while p2 < len(line):
                    # skip whitespace
                    if line[p2] == ' ' and p2 + 1 < len(line) and line[p2 + 1] == " ":
                        p2 += 1
                        continue
                    if line[p1] == ' ' and p1 + 1 < len(line) and line[p1 + 1] == " ":
                        p1 += 1
                        continue

                    elif line[p2] == "'":
                        if p2 - p1 > 1:
                            self.tokens.append((line[p1:p2], line_nr))
                        if p2 + 2 < len(line) or line[p2 + 2] != "'":
                            raise Exception("' is not matched - line" + str(line_nr))
                        self.tokens.append((line[p2:p2 + 3], line_nr))

                        # treat " case
                    elif line[p2] == '"':
                        match = Matcher.match_string(line[p2:])
                        if match is None:
                            raise Exception('" is not matched - line' + str(line_nr))
                        else:
                            # self.pif.append(("const", self.constSt.add(match.string)))
                            p2 += match.regs[0][1]  # get the end + 1 position of the first match
                            self.tokens.append((line[p1:p2], line_nr))
                            p1 = p2

                    # if current char is separator
                    elif line[p2] in self.separators:
                        # we have something before the separator
                        if p2 - p1 > 0:
                            self.tokens.append((line[p1:p2], line_nr))
                        if line[p2] != " ":
                            self.tokens.append((line[p2], line_nr))
                        p2 += 1
                        p1 = p2

                    elif line[p2] in self.operators:
                        if p2 - p1 > 0:
                            self.tokens.append((line[p1:p2], line_nr))
                        if p2 + 1 < len(line) and ((line[p2] == '<' or line[p2 + 1] == ">") and line[p2 + 1] == "="):
                            self.tokens.append(line[p2:p2 + 2])
                            p2 += 2
                            p1 = p2
                        elif p2 + 1 < len(line) and line[p2] == "-":
                            match = Matcher.match_int(line[p2:])
                            if match is not None:
                                p2 += match.regs[0][1]  # get the end + 1 position of the first match
                                self.tokens.append((line[p1:p2], line_nr))
                                p1 = p2
                                continue
                            else:
                                self.tokens.append(line[p2])
                                p2 += 1
                                p1 = p2
                        else:
                            self.tokens.append(line[p2])
                            p2 += 1
                            p1 = p2
                    else:
                        p2 += 1

                # reached end of line
                if p2 - p1 > 1:
                    self.tokens.append((line[p1:p2], line_nr))

                line = file.readline()

    def __classify(self, token):
        pass


class Matcher:

    @staticmethod
    def special_split(line):
        first = line.find('"')

    @staticmethod
    def match_int(s):
        return re.match("-*[1-9]+[0-9]*", s)

    @staticmethod
    def match_identifier(s):
        return re.match("[a-zA-Z]+[a-zA-Z1-9_]*", s)

    @staticmethod
    def match_string(s):
        return re.match('"[^\n"]*"', s)


st = ' fint = "vf d "'
f = st.find('"')
stb = sb.SymbolTable()
stb.add(re.match('"[^\n"]*"', '"fd da d " 3f').string)
# print(st.find('"', st.find('"', f + 1)))
scan = Scanner("p1")
scan.scan()
for t in scan.tokens:
    print(t[0])
