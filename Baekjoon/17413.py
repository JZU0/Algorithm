import sys 
import re 
 
start = [] 
end = []
str = sys.stdin.readline().rstrip()  
if '<' in str :
    bracket =re.compile('\<(.*?)\>')
    result = bracket.finditer(str) 
    for i in result:
        print(i)

#bracket ='\<[^)]*\>'
#text = re.sub(pattern=bracket, repl='',string=str)
#print(text) 
