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
 
""" 
d=map(int,open(0))
n=next(d)
data=sorted(d)
ans=max(data[-i]*(i) for i in range(1,n+1))
print(ans)
""" 
""" 
n,*l=map(int,open(0))
l.sort()
print(max(l[i]*(n-i) for i in range(n)))
"""