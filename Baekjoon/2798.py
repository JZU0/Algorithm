import sys  
from itertools import combinations
 
N, M = map(int, sys.stdin.readline().split())
 
cardTable = list(map(int, sys.stdin.readline().split()))
   
result = 0 
 
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            hap = cardTable[i] + cardTable[j] + cardTable[k]
            if hap <= M:
                result = max(result, hap)
 
print(result)