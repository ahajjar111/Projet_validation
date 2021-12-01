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