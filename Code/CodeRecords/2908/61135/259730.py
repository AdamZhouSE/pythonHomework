import sys
input=sys.stdin.readlines()
num=int(input[0])
s=set()
for index in range(1,num+1):
    s.add(len(input[index]))
print(len(s))