import sys  

N = int(sys.stdin.readline())
d = [list(map(int, sys.stdin.readline().split())) for i in range(N)] 
 
rank = [1]*(N) 
 
for i in range(N):
    for j in range(N):
        if (d[i][0] > d[j][0] and d[i][1] > d[j][1]):
                rank[j] += 1 
   
print(*rank)