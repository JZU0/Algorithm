#import sys 
 
#N, M = map(int, sys.stdin.readline().split())   
 
#*A, = map(int, sys.stdin.readline().split())   
#*B, = map(int, sys.stdin.readline().split())   
 
#print(*(sorted(A+B)))  

import sys
N,M = sys.stdin.readline().split()
print(' '.join(sorted(sys.stdin.read().split(), key=int)))  
 
# print(*(sorted(sys.stdin.read().split(), key=int))) 
# 시간이 오래 걸린다.