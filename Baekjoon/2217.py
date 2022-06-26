import sys 
 
n = int(input()) 
arr = []  
w_arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
 
for i in range(n,0,-1):  
    m = min(arr)
    w_arr.append(i*m) 
    arr.remove(m)

print(max(w_arr))