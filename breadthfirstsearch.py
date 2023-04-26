graph1 = {
    'A':['B','C','D'],
    'B':['E','F'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}
graph2 = {
    '0':['1','2','3','4'],
    '1':['0','2'],
    '2':['0','1','3','5'],
    '3':['0','2','4','5'],
    '4':['0','3','5'],
    '5':['2','3','4']
}

visited = []
queue = []   

def bfs(visited, graph, node):
  visited.append(node)
  
  
  queue.append(node)

 

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        
        queue.append(neighbour)

print("\n Graph1 for BFS")
bfs(visited, graph1, 'A')
print("\n Graph2 for BFS")
bfs(visited, graph2, '0')   
