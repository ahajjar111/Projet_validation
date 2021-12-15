from Kernel import STR2TR, isAcceptingProxy
from SoupLanguage import BehaviourSoup, BehSoupSemantics
from algorithms import predicate_model_checker


class CounterConfig:
    def __init__(self):
        self.pc = 0
    def __hash__(self):
        return hash(self.pc)
    def __eq__(self, other):
        return self.pc==other.pc
    
    def __repr__(self) -> str:
        return str(self.pc)


def counter(max):
    soup = BehaviourSoup(CounterConfig())
    def inc(c):
        c.pc = c.pc + 1
    soup.add('inc', lambda c: c.pc < max , inc)
    def reset(c):
        c.pc = 0
    soup.add('reset', lambda c: c.pc>=max , reset)

    return soup

if __name__ == '__main__':
    semantics = BehSoupSemantics(counter(3))
    # predicate_model_checker(semantics, lambda c: c.pc==2)
    # predicate_model_checker(semantics, lambda c: c.pc > 50)
    tr = STR2TR(semantics)
    tr = isAcceptingProxy(tr,lambda c: c.pc==2)
    print(tr.initial())
