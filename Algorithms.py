from Kernel import STR2TR, isAcceptingProxy, ParentStoreProxy


def bfs(graph):
    known = set()  # Known
<<<<<<< HEAD
<<<<<<< HEAD
    frontier = []  # Frontier #list_des_noeuds
=======
    frontier = []  # Deque()  Frontier #list_des_noeuds
>>>>>>> 95d2431edf26e6edcf8eb8b862e993814a838085
=======
    frontier = []  # Deque()  Frontier #list_des_noeuds
>>>>>>> 95d2431edf26e6edcf8eb8b862e993814a838085
    at_start = True  # init

    while frontier or at_start:
        if at_start:
            neighbours = graph.initial()
            at_start = False
        else:
            neighbours = graph.next(frontier.popleft())
        for n in neighbours:

            if n not in known:
                known.add(n)
                frontier.append(n)

    return known


def find_accepting_bfs(g):
    known = dict()
    frontier = []  # depue()
    at_start = True

    while frontier or at_start:
        if at_start:
            neighbours = g.initial()
            at_start = False
        else:
            g.next(frontier.pop(0))

        for n in neighbours:
            if n not in known:
                if g.is_accepting(n):
                    return True, n
                known[n] = n
                frontier.append(n)
    return False, n


def predicate_model_checker(semantics, predicate):
    tr = STR2TR(semantics)

    tr = isAcceptingProxy(tr, predicate)

    tr = ParentStoreProxy(tr)
    r = find_accepting_bfs(tr)
    get_trace(tr.parent, r, tr.initial())


def get_trace(parents, result, initial):
    status, target = result
    if not status:
        print("L'accepting state n'est pas trouvé ")
        return None
    print(initial, result)

    current_Node = target
    trace = [current_Node]
    while current_Node not in initial:
        current_Node = parents[current_Node]
        trace.append(current_Node)

    print("Trace : ", trace)
