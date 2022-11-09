# 1 a

class SymbolTable:

    def __init__(self):
        self.__capacity = 30
        self.__table = [[] for _ in range(self.__capacity)]

    def __hash(self, target):
        if isinstance(target, str):
            hash = 5381
            for ch in target:
                hash = ((hash << 5) + hash) + ord(ch)
            return hash % self.__capacity
        elif isinstance(target, int):
            return target % self.__capacity

    def add(self, value):
        hash = self.__hash(value)
        if value not in self.__table[hash]:
            pos = len(self.__table[hash])
            self.__table[hash].append(value)
            return hash, pos
        return hash, self.__table[hash].index(value)

    def lookup(self, value):
        key, val = value
        if len(self.__table[key]) == 0 or len(self.__table[key]) - 1 < val:
            return None
        else:
            return self.__table[key][val]

    def __iter__(self):
        return self.__table.__iter__()
