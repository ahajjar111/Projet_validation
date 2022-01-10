import source
from abc import ABC, abstractmethod
from kernel import STR2TR


class ostr(ABC):
    @abstractmethod
    def __init__(self, operand):
        self.operand = operand

    def initial(self):
        return self.operand.initial()

    def actions(self, c):
        return self.operand.actions(c)

    def execute(self, a):
        target = self.operand.execute(c, a)
        return (source, a, target), target


input(str)


def actions(self, source):
    sychronous_actions = []
    kripte_src, buchi_src = source
