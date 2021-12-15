def find_accepting_bfs(g):
    known = [] #set()
    frontier = [] #depue()
    at_start = True
    while frontier or at_start:
        if at_start:
            neighbours = g.initial()
            at_start = False
        else: g.next(frontier.pop(0))

        for n in neighbours:
            if g.is_accepting(n):
                return True,n
            if n not in known:
                known.append(n)
                frontier.append(n)
    return False,n

<<<<<<< HEAD
def predicate_model_checker(semantics, predicate):
    return True
=======
    #testing
>>>>>>> 8a9a6261d4d1699df498ea6a96e2297482f2c3a8
