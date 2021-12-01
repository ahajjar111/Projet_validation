def is_safe_bfs(g):
    known = [] #set()
    frontier = [] #depue()
    acct_start = True
    while frontier or acct_start:
        if acct_start:
            neighbours = g.initial()
        else g.next(frontier.popleft())
    for n in neighbours:
        if g.is_accepting(n):
            return False
        if n not in known:
            known.append(n)
            frontier.append(n)
