import sys 
 
N, M = map(int, sys.stdin.readline().split())   
 
*A, = map(int, sys.stdin.readline().split())   
*B, = map(int, sys.stdin.readline().split())   
 
print(*sorted(A+B))