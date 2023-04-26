from queue import PriorityQueue
v1 = 14
v2 = 10
graph1 = [[] for i in range(v1)]
graph2 = [[] for i in range(v2)]
def best_first_search(actual_Src, target, n,graph):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True
 
    while pq.empty() == False:
      u = pq.get()[1]
      print(u,end="")
      
      if u == target:
          break
 
      for v, c in graph[u]:
          if visited[v] == False:
              visited[v] = True
              pq.put((c, v))
    print()
 
 
 
def addedge(x, y, cost):
    graph1[x].append((y, cost))
    graph1[y].append((x, cost))
 
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

source1 = int(input("enter the source 1"))
target1 = int(input("enter a target 1"))
best_first_search(source1, target1, v1,graph1)

def addedge(x, y, cost):
    graph2[x].append((y, cost))
    graph2[y].append((x, cost))

addedge(0, 1, 3)
addedge(0, 2, 2)
addedge(1, 3, 7)
addedge(1, 4, 4)
addedge(2,5,5)
addedge(2,6,3)
addedge(5,7,10)
addedge(6,8,5)
addedge(6,9,6)


source2 = int(input("enter the source 2"))
target2 = int(input("enter a target 2"))
best_first_search(source2, target2, v2,graph2)






