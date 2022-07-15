import sys 
 
from itertools import permutations
 
n = int(sys.stdin.readline()) 
k = int(sys.stdin.readline()) 
 
arr = [] 
card = set() 

for i in range(n):
    arr.append(sys.stdin.readline().rstrip())
   
for k in permutations(arr, k): 
    card.add("".join(k))
 
print(len(card)) 
 
''' 
import sys
import itertools

n,k,*c = map(int, sys.stdin.readlines())
c = list(map(str, c))

x = list()

for y in list(itertools.permutations(c,k)):
    x.append("".join(y))

print(len(set(x)))
'''

 

                    