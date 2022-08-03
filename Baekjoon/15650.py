import sys  
import itertools
 
N, M = map(int, sys.stdin.readline().split())   
 
arr = [] 

for i in range(1,N+1):
    arr.append(str(i))   

print("\n".join(list(map(" ".join,itertools.combinations(arr,M))))) 

#for i in itertools.permutations(arr,M):
#    print(*list(i))