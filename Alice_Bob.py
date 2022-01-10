from Kernel import *
from SoupLanguage import *
from Algorithms import *

# import inspect


class Alice_Bob_Conf:

    def __init__(self):
        self.apc = 0
        self.bpc = 0

    def __hash__(self):
        return int(hash(self.apc + self.bpc)) 

    def __eq__(self, other):
        return self.apc == other.apc & self.bpc == other.bpc

    def __repr__(self):
        return str(self.apc) + str(self.bpc)


def Alice_Bob(maxi):
    
    soup = BehaviourSoup(Alice_Bob_Conf())

    def aToSc(c):
        c.apc = 1

    soup.add("aToSc", lambda c: c.apc == 0, aToSc)

    def bToSc(c):
        c.bpc = 1

    soup.add("bToSc", lambda c: c.bpc == 0, bToSc)

    def aToInit(c):
        c.apc = 0

    soup.add("aToInit", lambda c: c.apc == 1, aToInit)

    def bToInit(c):
        c.bpc = 0

    soup.add("bToInit", lambda c: c.bpc == 1, bToInit)


    #def Alice_BobToSc(c):
    #    c.apc = 1
    #    c.bpc = 1

    #soup.add("Alice_BobToSc", lambda c: c.apc + c.bpc == maxi, Alice_BobToSc)

    return soup


if __name__ == "__main__":
    semantics = BehSoupSemantics(Alice_Bob(2))
    # print(semantics.initial())
    # print(semantics.actions(semantics.initial()[0]))

    # for action in semantics.actions(semantics.initial()[0]):
    #     print(inspect.getsource(action))

    # print(inspect.getsource(semantics.actions(semantics.initial()[0]) ))

    r = bfs(STR2TR(semantics))
    print("Etats: ", r) 

    predicate_model_checker(semantics, lambda c: c.bpc == 0)

    print("Test de deadlock: ", end=" ")
    predicate_model_checker(semantics, lambda c: len(semantics.actions(c)) == 0 )
    print("Test de la section critique: ", end=" ")
    predicate_model_checker(semantics, lambda c: c.apc == 1 and c.bpc == 1 )