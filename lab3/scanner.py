# doc: regex, uml diagram, something else
import re


class Scanner:

    def __init__(self):
        self.operators = ['+', '-', '*', '/', '<', '<=', '=', '>=', 'eq', 'mod', 'not']
        self.keywords = ['init', 'verify', 'otherwise', 'escape', 'true', 'untrue', 'while', 'for', 'func', 'in']
        self.separators = [']', '[', '{', '}', ';', ' ', '"', "'"]
        self.pif = ()
        self.st = ()
        self.constSt = ()

    def __readFile(self):
        pass

    def scan(self, filename):
        pass

    def __classify(self, token):
        pass


def special_split(line):
    first = line.find('"')


with open('p1') as file:
    line = file.readline()
    while line:
        if '"' in line:
            special_split(line)
        else:
            line.split()

        line = file.readline()


def match_int(s):
    return re.match("-*[1-9]+[0-9]*",s)

def match_identifier(s):
    return re.match("[a-zA-Z]+[a-zA-Z1-9_]*",s)

st = ' fint = "vf d "'
f =st.find('"')
print(st.find('"',st.find('"',f+1)))



