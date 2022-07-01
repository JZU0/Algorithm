from sys import stdin
input = stdin.readline

line = input().rstrip().replace('>','<').split('<')
s=''

for i,word in enumerate(line):
    if i%2==1:
        s += '<'+word+'>'
    else:
        reverse_word = [w[::-1] for w in word.split()]
        s += ' '.join(reverse_word)
print(line)
print(s)