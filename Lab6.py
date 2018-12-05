#CS2302
#Aaron Brown
#Diego Aguirre
#Anindita Nath
#12/4/18
#implement topological sort and kruskals algorithm
from queue import Queue
from Graphs.GraphAM import GraphAM
from Graphs.GraphAL import GraphAL
from DisjointSetForest import DisjointSetForest

def topological_sort(graph):# returns a list of vertices in order
    all_in_degrees = compute_indegree_every_vertex(graph)
    sort_result = []
    q = Queue()

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.put(i)

    while not q.empty():
        u = q.get()
        sort_result.append(u)

        for adj_vertex in graph.get_vertices_reachable_from(u):
            all_in_degrees[adj_vertex] -= 1
            if all_in_degrees[adj_vertex] == 0:
                q.put(adj_vertex)

    if len(sort_result) != graph.get_num_vertices():
        return None

    return sort_result

def compute_indegree_every_vertex(graph):
    indegrees = []

    for i in range(graph.get_num_vertices()):
        indegrees.append(len(graph.get_vertices_that_point_to(i)))

    return indegrees


def kruskals_algorithm(graph):#returns minimum spanning tree
    edges = []

    for vertex in range(graph.get_num_vertices()):
        for adj_vertex in graph.get_vertices_reachable_from(vertex):
            edges.append([graph.get_edge_weight(vertex ,adj_vertex) , adj_vertex , vertex ]) #edges stored as weight, destination vertex ,source vertex

    edges.sort()  #sort edges by weight
    dsf = DisjointSetForest(graph.get_num_vertices())
    T = []

    for i in range(len(edges)):
        src = edges[i][2]
        dest = edges[i][1]
        if createsCycle(dsf,src,dest) == False:
            T.append(edges[i])
            dsf.union(edges[i][2] , edges[i][1])

    for i in range(len(T)):
        T[i].reverse()  #edges stored as source , destination , weight

    return T


def createsCycle(dsf,src,dest):
        if dsf.find(src) == dsf.find(dest):
            return True
        return False


def main():
    graph = GraphAM(5,True)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,4)
    #graph.add_edge(4,1) #creates cycle

    print('Minimum Spanning Tree from Kruskals Algorithm')
    print('source  destination  weight')
    minimumSpanningTree = kruskals_algorithm(graph)
    for i in range(len(minimumSpanningTree)):
        print(minimumSpanningTree[i])
    print('Topological Sort')
    print(topological_sort(graph))

main()

