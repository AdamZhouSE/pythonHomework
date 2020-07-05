import sys
words=[]
rw=sys.stdin.readlines()
for line in rw:
    words.append(line.replace('\n',''))
print(words)