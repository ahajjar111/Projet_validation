from Kernel import TransitionRelation


class SimpleGraph(TransitionRelation):
    def __init__(self, g, iniS):
        self.g = g
        self.iniS = iniS
    
    def initial(self):
        return self.iniS
    
    def next(self, c):
        try:
            return self.g[c]
        except:
            KeyError:
            return[]
