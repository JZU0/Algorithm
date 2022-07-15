import sys 
 
N = int(sys.stdin.readline()) 
   
tmp = N+1

for i in range(1,N+1):
    total = i 
    for j in str(i):
        total += int(j)  
    if total == N: 
        if (tmp > i): 
            tmp = i   
if tmp == N+1 :
    print(0) 
else :  
    print(tmp)