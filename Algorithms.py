from Kernel import STR2TR, isAcceptingProxy, ParentStoreProxy
from typing import Deque

def bfs(g):
    known = set()
    frontier = Deque() 
    at_start = True  # init

    while frontier or at_start:
        if at_start:
            neighbours = g.initial()
            at_start = False
        else:
            neighbours = g.next(frontier.popleft())
        for n in neighbours:
            
            if n not in known:
                known.add(n)
                frontier.append(n)

    return known

def find_accepting_bfs(g):

    known = dict() 
    frontier = Deque()
    at_start = True

    while frontier or at_start:
        if at_start:
            neighbours = g.initial()
            at_start = False
        else: neighbours = g.next(frontier.popleft())

        for n in neighbours:
            if n not in known:
                if g.is_accepting(n):
                    return True,n
                known[n] = n
                frontier.append(n)
    return False,None

def is_bfs_reachable(g, start, end):
    known = set()
    frontier = Deque()
    neighbours = [start]

    for i in neighbours:
        if i not in known:
            known.add(i)
            frontier.append(i)

    while frontier:
        neighbours = g.next(frontier.popleft())

        for i in neighbours:
            if i == end:
                return True
            if i not in known:
                known.add(i)
                frontier.append(i)

    return False


def is_bfs_safe(graph):
    known = set()
    frontier = Deque()
    at_start = True
    
    while frontier or at_start:
        if at_start:
            neighbours = [graph.initial()]
            at_start = False
        else:
            neighbours = graph.next(frontier.popleft())
        for n in neighbours:
            
            if n not in known:
                if graph.is_accepting(n):
                    return False
                known[n] = n
                frontier.append(n)

    return True


def predicate_model_checker(semantics, predicate):
    tr = STR2TR(semantics)

    tr = isAcceptingProxy(tr, predicate)

    tr = ParentStoreProxy(tr)
    r = find_accepting_bfs(tr)
    get_trace(tr.parent, r, tr.initial())

def get_trace(parents, result, initial):
    status,target = result
    if not status :
        print("L'accepting state n'est pas trouvé ")
        return None
    print (initial,result)

    current_Node = target
    trace = [current_Node]
    while current_Node not in initial:
        current_Node = parents[current_Node]
        trace.append(current_Node)

    print("Trace : ", trace)