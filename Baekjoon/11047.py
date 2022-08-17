import sys 

N, K = map(int, sys.stdin.readline().split())    
  
list = [] 

for i in range(N):
    list.append(int(sys.stdin.readline())) 
  
cnt = 0
for i in reversed(range(N)):
    cnt += K // list[i] 
    K %= list[i] 
    if K == 0:
        break 
 
print(cnt)
