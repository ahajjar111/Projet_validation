def is_safe_bfs(g):
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