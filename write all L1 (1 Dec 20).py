import networkx as nx
import timeit
import ast
import re
import gzip

source = open("graph_catalogue/graph10.txt","r")
target = open("graph10_L1.txt", "w")
element_number = 10

counter = 0


def is_los(arg1):

    G = nx.Graph()
    G.add_nodes_from(list(range(0,element_number)))
    G.add_edges_from(arg1)

    X = list(G.nodes)


    def is_orthogonal(arg1, arg2):
        return all(arg1 in G.neighbors(arg2[i]) for i in range(0, len(arg2)))


    def complement(lst1, lst2):
        return list(set(lst1).difference(set(lst2)))


    def orth_compl(arg1):  # arg1 is list here
        t = []
        for item in X:
            if is_orthogonal(item, arg1):
                t.append(item)
        return t


    ###### MAIN CODE ######

    for item1 in X:

        for item2 in [x for x in X if x != item1]:  # that means f is different than e

            if not is_orthogonal(item1, [item2]):

                if any(orth_compl([item1, item2]) == orth_compl([item1, item3]) for item3 in orth_compl([item1])) is False:

                    return False

    else:

        return True


def write_all_los():
    for line in source:
        global counter
        counter = counter + 1
        if counter % 100 == 0:
            print("checked " + str(counter))
        #line = line.rstrip()
        #line2 = ast.literal_eval(line)
        b = re.findall('\d+', line)
        c = list(map(int, b))
        line2 = [[c[i], c[i + 1]] for i in range(0, len(c), 2)]
        if is_los(line2):
            print(line2, file=target)
            print(line2)

    print(timeit.default_timer())

write_all_los()



