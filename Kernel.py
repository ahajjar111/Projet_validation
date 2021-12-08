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


class semanticTransitionRelations:
    def __init__(self):
        pass

    def actions(self, conf):
        pass

    def execute(self, conf, actions):
        pass

class BehSoupSemantics(semanticTransitionRelations):
    def initial(self):
        return [soup.initial]

    def actions(self, conf):
        return list(map(lambda beh : beh.action,
                         filter(lambda beh: beh.guard(conf),
                         self.soup.behaviours)))

    def execute(self, c, a):
        target = copy.deepcopy(c)
        r = a(target)
        return target
