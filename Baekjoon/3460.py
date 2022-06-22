n = int(input())  
n_list = [] 
r_list = []  
 
for i in range(0,n):
    num = int(input())
    n_list.append(num) 
for k in n_list:
    while k > 0 :
        r = k % 2  
        r_list.append(r)
        k //= 2   
    idx = 0 
    for j in r_list: 
        if j==1 : 
            print(str(idx)+" ",end="") 
        idx += 1  
    r_list.clear() 
    print()

