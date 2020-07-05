input=input()
a=list()
b=list()
num=0
for x in range(0,len(input)):
    if input[x]=='Q':
        a.append(x)
    if input[x]=='A':
        b.append(x)
for y in range(0,len(b)):
    index=0
    while a[index]<b[y]:
        index=index+1
    num=num+index*(len(a)-index)
print(num,end='')