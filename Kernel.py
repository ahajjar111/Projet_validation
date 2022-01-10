import copy
class TransitionRelation:

    def __init__(self):
        pass

    def next(self, c):
        pass

class AcceptingSet:
    def is_accepting(self,c):
        pass

class identifyProxy:
    def __init__(self, operand):
        self.operand = operand

    def __getattr__(self, attr):
        return getattr(self.operand, attr)

    def initial(self):
        return self.operand.initial()
    
    def next(self, c):
        return self.operand.next(c)
    

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

    def initial (self):
        pass

    def actions(self, conf):
        pass

    def execute(self, conf, actions):
        pass

class BehSoupSemantics(semanticTransitionRelations):
    def __init__(self, program):
        self.soup = program
    def initial(self):
        return [self.soup.initial]

    def actions(self, conf):
        return list(map(lambda beh : beh.action,
                         filter(lambda beh: beh.guard(conf),
                         self.soup.behaviours)))

    def execute(self, c, a):
        target = copy.deepcopy(c)
        r = a(target)
        return target

class STR2TR:
    def __init__(self, str):
        self.operand = str

    def initial(self):
        return self.operand.initial()
    
    def next(self, c):
        targets = []
        for a in self.operand.actions(c):
            target = self.operand.execute(c,a)
            targets.append(target)
        return targets


class isAcceptingProxy(identifyProxy):
    def __init__(self, operand, predicate):
        super().__init__(operand)
        self.predicate = predicate
    
    def is_accepting(self, c):
        return self.predicate(c)
