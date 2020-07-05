num=int(input())
temp=[]
while num!=0:
    temp.append(num%2)
    num=num//2
max=0
current=0
while 1 in temp:
    current=temp.index(1)
    temp[current]=0
    if not 1 in temp:
        break
    find=temp.index(1)
    if find-current>max:
        max=find-current
    current=find
print(max)