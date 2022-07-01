import sys
 
n = int(sys.stdin.readline())
*switch, = map(int, sys.stdin.readline().split()) 
 
n2 = int(sys.stdin.readline())  
 
for _ in range(n2):
    a, b = map(int, sys.stdin.readline().split())   
    print(a,b)