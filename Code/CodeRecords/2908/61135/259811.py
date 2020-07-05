import sys
input=sys.stdin.readlines()
num=int(input[0])
s=set()
for index in range(1,num+1):
    a=input[index].replace(' ','')
    b=a.replace('\n','')
    c=list(b)
    c.sort()
    d="".join(c)
    s.add(d)
print(len(s),end='')
