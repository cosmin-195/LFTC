import Grammar
import copy


class Parser:

    def __init__(self, grammar: Grammar):
        self.grammar = grammar

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


g = Grammar.Grammar()
g.read_from_file("exempleCFG")
p = Parser(g)
print(p.closure(["Z->.S"]))
