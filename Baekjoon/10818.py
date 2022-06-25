n = int(input()) 
list = list(map(int, input().split())) 
 
print(min(list),end=" ") 
print(max(list)) 
 
'''  
import sys

n, *m = map(int, sys.stdin.read().split())

print(min(m), max(m))
'''