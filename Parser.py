import Grammar
import copy


class Parser:

    def __init__(self, grammar: Grammar):
        self.grammar = grammar

    def closure(self, S):
        result = set()
        added_all_prod_of_nonterminal = {}
        for n in self.grammar.N:
            added_all_prod_of_nonterminal[n] = False
        for item in S:
            left, right = item.split("->")
            if "." in right:
                leftSideOfDot, rightSideOfDot = right.split(".".split())
                nonterminal = rightSideOfDot[rightSideOfDot.find(".")+1]
                if not added_all_prod_of_nonterminal[nonterminal]:




