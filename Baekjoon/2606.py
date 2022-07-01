import sys 

cnt = 0
def DFS(graph, start, visited = []): 
    global cnt
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            DFS(graph, node, visited)  
            cnt += 1
    
N= int(sys.stdin.readline())
link = int(sys.stdin.readline())

graph = [[]*(N+1) for _ in range(N+1)]

for i in range(link):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(1)
print(cnt)