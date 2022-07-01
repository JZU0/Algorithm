import sys, re

str = re.split('<|>', sys.stdin.readline().rstrip())   
print(str)

result = '' 

for i in range(len(str)):
    if i % 2 == 1:
        result += '<'+str[i]+'>'
    else:
        result += ' '.join(w[::-1] for w in str[i].split())

print(result) 
