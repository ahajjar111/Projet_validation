from Kernel import *
from SoupLanguage import *
from Algorithms import *

# import inspect

class Alice_Bob_Conf:

    def __init__(self):
        self.apc = 0
        self.bpc = 0
        self.DrapeauAlice = 0
        self.DrapeauBob = 0
    def __hash__(self):
        return int(hash(self.apc + self.bpc)+hash(self.DrapeauAlice + self.DrapeauBob))

    def __eq__(self, other):
        return self.apc == other.apc and self.bpc == other.bpc and self.DrapeauAlice == other.DrapeauAlice and self.DrapeauBob == other.DrapeauBob

    def __repr__(self):
        return str(self.apc) + str(self.bpc)


def Alice_Bob():
    soup = BehaviourSoup(Alice_Bob_Conf())

    def aToWait(c):
        c.apc = 1
        c.DrapeauAlice = 1
    soup.add("aToWait", lambda c: c.apc == 0, aToWait)

    def aToSC(c):
        c.apc = 2
        c.DrapeauAlice = 1

    soup.add("aToSC", lambda c: c.apc == 0 and c.bpc !=2,  aToSC)
    def aToInit(c):
        c.apc = 0
        c.DrapeauAlice=0

    soup.add("aToInit", lambda c: c.apc == 2, aToInit)

    def bToSc(c):
        c.bpc = 2
        c.DrapeauBob= 1
    soup.add("bToSc", lambda c: c.bpc == 0 and c.apc != 2, bToSc)

    def bToWait(c):
        c.bpc = 1
        c.DrapeauBob = 1
    soup.add("bToWait", lambda c: c.bpc == 0, bToWait)

    def bToInit(c):
        c.bpc = 0
        c.DrapeauBob = 0

    soup.add("bToInit", lambda c: c.bpc == 2, bToInit)

    return soup


if __name__ == "__main__":
    semantics = BehSoupSemantics(Alice_Bob())
    # print(semantics.initial())
    # print(semantics.actions(semantics.initial()[0]))

    # for action in semantics.actions(semantics.initial()[0]):
    #     print(inspect.getsource(action))

    # print(inspect.getsource(semantics.actions(semantics.initial()[0]) ))

    # r = bfs(STR2TR(semantics))
    # print("Etats: ", r)

    #predicate_model_checker(semantics, lambda c: c.bpc == 0)

    print("Test de deadlock: ", end=" ")
    predicate_model_checker(semantics, lambda c: len(semantics.actions(c)) == 0)
    print("Test de la section critique: ", end=" ")
    predicate_model_checker(semantics, lambda c: c.apc == 2 and c.bpc == 2)