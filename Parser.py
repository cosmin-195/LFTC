import Grammar
import copy


class Parser:

    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.table = []

    def closure(self, S):
        result = []
        for item in S:
            result.append(item)
        added_all_prod_of_nonterminal = {}
        for n in self.grammar.N:
            added_all_prod_of_nonterminal[n] = False
        notDone = False
        while (not notDone):
            for item in result:
                notDone = True
                left, right = item.split("->")
                if "." in right:
                    leftSideOfDot, rightSideOfDot = right.strip().split(".")
                    nonterminal = rightSideOfDot[rightSideOfDot.find(".") + 1]
                    if nonterminal in self.grammar.N:
                        if not added_all_prod_of_nonterminal[nonterminal]:
                            added_all_prod_of_nonterminal[nonterminal] = True
                            for production in self.grammar.P[nonterminal]:
                                result.append(nonterminal + " -> ." + production)
                                notDone = False
        return result

    def parse(self, seq):
        work_stack = [0]
        input_stack = seq
        input_stack_pointer = 0
        work_stack_pointer = 0
        output_stack = []

        # pop work stack
        while True:
            popped = work_stack[work_stack_pointer]
            from_input = input_stack[input_stack_pointer]
            input_stack_pointer = +1
            action = self.table.pop()[0]
            if action == 's':
                next_state = self.table[popped][1][from_input]
                work_stack.append(action)
                work_stack.append(next_state)
            # reduce



g = Grammar.Grammar()
g.read_from_file("exempleCFG")
p = Parser(g)
print(p.closure(["Z->.S"]))
