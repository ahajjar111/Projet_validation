from Kernel import STR2TR, isAcceptingProxy, ParentStoreProxy

def find_accepting_bfs(g):

    known = dict() 
    frontier = [] #depue()
    at_start = True

    while frontier or at_start:
        if at_start:
            neighbours = g.initial()
            at_start = False
        else: g.next(frontier.pop(0))

        for n in neighbours:
            if n not in known:
                if g.is_accepting(n):
                    return True,n
                known[n] = n
                frontier.append(n)
    return False,n

def predicate_model_checker(semantics, predicate):
    tr = STR2TR(semantics)

    tr = isAcceptingProxy(tr, predicate)

    tr = ParentStoreProxy(tr)
    r = find_accepting_bfs(tr)

