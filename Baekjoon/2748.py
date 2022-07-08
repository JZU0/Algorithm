import sys 
 
n = int(sys.stdin.readline()) 
  
arr = [0]*(n+1) 

arr[0] = 0 
arr[1] = 1  

def fib (i) :
    arr[i] = arr[i-1] + arr[i-2] 

if n > 1 : 
    for i in range(2,n+1):
        fib(i)  
         
print(arr[n]) 
 
'''
a=int(input())

tmp=[]

for i in range(a+1) :
    if i == 0 :
        tmp.append(0)
    elif i == 1:
        tmp.append(1)
    else :
        tmp.append(tmp[i-1]+tmp[i-2])

print(tmp[a])
'''
