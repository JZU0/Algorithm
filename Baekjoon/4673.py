arr = [] 

for i in range(1,10001): 
    hap = 0
    for j in str(i): 
        hap += int(j)
    arr.append(i+hap)
 
for i in range(1,10001):
    if i not in arr:
        print(i)