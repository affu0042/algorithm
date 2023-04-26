def aStarAlgo(start_node, stop_node, graph):
    open_set = set(start_node)
    closed_set = set()
    g = {}               
    parents = {}         
    g[start_node] = 0

    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or graph[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n, graph):

                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None
        

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return None
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

def get_neighbors(v, graph):

    if v in graph:
        return graph[v]
    else:
        return None

def heuristic(n):
    if n in Graph_nodes1:
        H_dist = {
            'A': 11,
            'B': 6,
            'C': 5,
            'D': 7,
            'E': 3,
            'F': 6,
            'G': 5,
            'H': 3,
            'I': 1,
            'J': 0
        }
    else:
        H_dist = {
            'A': 14,
            'B': 12,
            'C': 11,
            'D': 6,
            'E': 4,
            'F': 11,
            'Z': 0
        }
    return H_dist[n]



Graph_nodes1 = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3),('D', 2)],
    'C': [('E', 5),('D', 1)],
    'D': [('E', 8),('C', 1),('B', 2)],
    'E': [('I', 5),('C', 5),('D', 8),('J', 5)],
    'F': [('A', 3),('H', 7),('G', 1)],
    'G': [('F', 1),('I', 3)],
    'H': [('I', 2),('F', 7)],
    'I': [('H', 2),('G', 3),('J', 3),('E', 5)],
    'J': [('E', 5),('I', 3)]
}

Graph_nodes2 = {
    'A': [('B', 4), ('C', 3)],
    'B': [('A', 4),('E', 12),('F', 5)],
    'C': [('A', 3),('D', 7),('E', 10)],
    'D': [('E', 2),('C', 7)],
    'E': [('C', 10),('D', 2),('Z', 5)],
    'F': [('B', 5),('Z', 16)],
    'Z': [('F', 16),('E', 5)]
}

start_node=input("Enter Start node: ").upper()
goal_node=input("Enter Goal Node: ").upper()

aStarAlgo(start_node,goal_node,Graph_nodes1)

start_node=input("Enter Start node: ").upper()
goal_node=input("Enter Goal Node: ").upper()

aStarAlgo(start_node,goal_node,Graph_nodes2)
