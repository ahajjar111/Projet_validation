import networkx as nx
import matplotlib.pyplot as plt
import string


def execute(R, start):
    K = []
    F = []
    i = True
    while len(F) > 0 or i:
        N = []
        if not i:
            N = R[(F.pop(0))]
        else:
            N.extend(start)
            i = False
        for n in N:
            if n not in K:
                K.append(n)
                F.append(n)
    return K


def create_node(graph, nom, identifiant, donnee):
    graph.add_node(nom, id=identifiant, data=donnee)


def create_edge(graph, src, dest):
    graph.add_edge(src, dest)


g = nx.DiGraph()

nbNoeuds = 5
nbEdges = 5

listeAlphabets = list(string.ascii_lowercase)

for i in range(0, nbNoeuds):
    create_node(g, listeAlphabets[i], listeAlphabets[i], None)

print(g.nodes)

create_edge(g, "a", "b")
create_edge(g, "a", "c")
create_edge(g, "b", "d")
create_edge(g, "d", "e")
create_edge(g, "c", "e")

# for i in range(0, nbEdges):
#     print("Edge from src to destination ")
#     source = input("Edge source: ")
#     destination = input("Edge destination: ")
#     print(type(source), type(destination),)
#     create_edge(g, source, destination)
# 

K = execute(g, ["a"])
print("known", K)

nx.draw(g, with_labels=True)
plt.show()
