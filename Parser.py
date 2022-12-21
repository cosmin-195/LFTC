import Grammar
import copy


# lr0

class Table:

    def __init__(self):
        self.row_headers = []
        self.row_values = {}


class Parser:

    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.table = Table()
        self.productions = []
        self.__prepare_productions()
        self.fakeSymbol = self.grammar.S + "_PRIME"

    def closure(self, S):
        result = []
        for item in S:
            result.append(item)
        added_all_prod_of_nonterminal = {}
        for n in self.grammar.N:
            added_all_prod_of_nonterminal[n] = False
        notDone = False
        while (not notDone):
            notDone = True
            for item in result:
                left, right = item.split("->")
                if "." in right:
                    leftSideOfDot, rightSideOfDot = right.strip().split(".")
                    rightSideOfDot = rightSideOfDot.strip()
                    if len(rightSideOfDot) > 0:
                        nonterminal = rightSideOfDot[0]
                        if nonterminal in self.grammar.N:
                            if not added_all_prod_of_nonterminal[nonterminal]:
                                added_all_prod_of_nonterminal[nonterminal] = True
                                for production in self.grammar.P[nonterminal]:
                                    result.append(nonterminal + "->." + production)
                                    notDone = False
        return result

    def goto(self, S, x):
        closureInput = []
        for item in S:
            left, right = item.split("->")
            if "." in right:
                leftSideOfDot, rightSideOfDot = right.strip().split(".")
                rightSideOfDot = rightSideOfDot.strip()
                if len(rightSideOfDot) == 0:
                    continue
                if rightSideOfDot.find(x) == 0:
                    newItem = left.strip() + "->" + leftSideOfDot.strip() + x + "." + rightSideOfDot[len(x):]
                    closureInput.append(newItem)
        return self.closure(closureInput) if len(closureInput) > 0 else []

    def canonical_collection(self):
        start_item = self.grammar.S + "_PRIME->." + self.grammar.S
        c = []
        c.append(self.closure([start_item]))
        index = 0
        modified = True

        if len(c[0]) == 1 and c[0][0].find('.') == len(c[0][0]) - 1:
            if c[0][0].split("->")[0] == self.fakeSymbol:
                # its an accept
                self.table.row_headers.append('a')
            else:
                self.table.row_headers.append("r" + str(self.productions.index(c[0][0][:-1])))
        else:
            self.table.row_headers.append('s')

        while modified:
            modified = False
            for j, item_set in enumerate(c[index:]):
                for symbol in self.grammar.N + self.grammar.E:
                    result = self.goto(item_set, symbol)

                    if len(result) > 0:
                        if result in c:
                            idx = c.index(result)
                        else:
                            c.append(result)
                            modified = True
                            idx = -1
                            # add a new row to table
                        if len(result) == 1 and result[0].find('.') == len(result[0]) - 1:
                            if result[0].split("->")[0] == self.fakeSymbol:
                                # its an accept
                                if idx == -1:  # only create row if it doesn't exist
                                    self.table.row_headers.append('a')
                            else:
                                #  reduce
                                if idx == -1:
                                    self.table.row_headers.append("r" + str(self.productions.index(result[0][:-1])))
                        else:
                            # shift
                            if idx == -1:  # only create row if it doesn't exist
                                self.table.row_headers.append('s')
                            # else:
                            self.table.row_values[(j, symbol)] = idx
        return c

    def __prepare_productions(self):
        for prod in self.grammar.P:
            for right_side in self.grammar.P[prod]:
                self.productions.append(prod + "->" + right_side)

    def parse(self, seq):
        work_stack = [0]
        input_stack = seq
        input_stack_pointer = 0
        output_stack = []

        # pop work stack
        while True:
            popped = work_stack[len(work_stack) - 1]
            action = self.table.row_headers[popped]
            if action == 's':
                from_input = input_stack[input_stack_pointer]
                input_stack_pointer += 1
                next_state = self.table.row_values[(popped, from_input)]
                work_stack.append(from_input)
                work_stack.append(next_state)
            if action[0] == 'r':
                prodId = int(action[1:])
                prod = self.productions[prodId]
                left, right = prod.split('->')
                work_stack = work_stack[:len(work_stack) - len(right * 2)]
                work_stack.append(left)
                work_stack.append(self.table.row_values[work_stack[-2], work_stack[-1]])
            if action == 'a':
                print('good job')
                break


g = Grammar.Grammar()
# g.read_from_file("exampleCFG")
g.read_from_file("grammarFromS9")
p = Parser(g)
# print(p.closure(["E_PRIME->.E"]))
for i in p.canonical_collection():
    print(i)
print(p.table.row_headers)
print(p.table.row_values)
# print(p.closure(["Z->.S"]))
# print(p.goto(["Z->.S"], "S"))
