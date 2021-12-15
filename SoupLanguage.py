import copy

from Kernel import semanticTransitionRelations

class BehaviourSoup:
    def __init__(self,conf):
        self.initial = conf
        self.behaviours = []
        
    def add(self,n, g, a):
        self.behaviours.append(Behaviour(n,g,a))


class Behaviour:
    def __init__(self,name, g, a):
        self.name = name
        self.action = a
        self.guard = g

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