from _typeshed import Self
from Kernel import AcceptingSet, TransitionRelation


class SimpleGraph(TransitionRelation):
    def __init__(self, g, iniS):
        self.g = g
        self.iniS = iniS
    
    def initial(self):
        return self.iniS
    
    def next(self, c):
        try:
            return self.g[c]
        except KeyError:
            return[]

class NFA(SimpleGraph, AcceptingSet):
    def __init__(self, g, iniS, acc):
        super().__init__(g, iniS)
        self.accepting = acc

    def is_accepting (self,c):
        return c in self.accepting
        # if c in self.accepting:
        #     return True
