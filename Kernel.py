class TransitionRelation:

    def __init__(self):
        pass

    def next(self, c):
        pass

class AcceptingSet:
    def is_accepting(c):
        pass

class identifyProxy:
    def __init__(self, operand):
        self.operand = operand

    def __getattribute__(self,attr):
        return getattr(self.operand, attr)

class ParentStoreProxy(identifyProxy):
    def __init__(self, operand):
        super().__init__(operand)
        self.parent = {}
    
    def next(self, conf):
        ns = self.operand.next(conf)
        for n in ns:
            if n not in self.parents:
                self.parents[n]=conf,None
        return ns