from Kernel import semanticTransitionRelations


class BuchiSemantics(semanticTransitionRelations):
    def __init__(self, d):
        super(BuchiSemantics).__init__()
        self.delta = d

    def initial(self):
        return self.initial()

    def actions(self,i,c):
        actives = []
        actions = self.delta[c]
        for a in actions:
            if a[0](i):
                actives.append(a)
        return actives


def execute(self, i, c, a):
    return a[i]


