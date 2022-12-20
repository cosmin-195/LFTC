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
        while modified:
            modified = False
            for item_set in c[index:]:
                for symbol in self.grammar.N + self.grammar.E:
                    result = self.goto(item_set, symbol)
                    if len(result) > 0 and result not in c:
                        c.append(result)
                        modified = True
        return c


g = Grammar.Grammar()
# g.read_from_file("exampleCFG")
g.read_from_file("grammar4.1")
p = Parser(g)
# print(p.closure(["E_PRIME->.E"]))
for item in p.canonical_collection():
    print(item)
# print(p.closure(["Z->.S"]))
# print(p.goto(["Z->.S"], "S"))
