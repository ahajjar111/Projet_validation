from abc import ABC, abstractmethod


class ostr(ABC):
    @abstractmethod
    def __init__(self, operand):
        self.operand = operand

    def initial(self):
        return self.operand.initial()

    def actions(self, c):
        return self.operand.actions(c)

    def execute(self, c, source, a):
        target = self.operand.execute(c, a)
        return (source, a, target), target
