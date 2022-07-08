import sys  
import math
         
for i in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())  
    print(int(math.factorial(M)/(math.factorial(N)*math.factorial(M-N))))