global subUnion
subUnion=list()

def subUnionCAL(last):
    for i in range(len(last)):
        temp=""
        for j in last[i:]:
            temp=temp+j
            subUnion.append(temp)

n=int(input())
first=input()
left=list()
i=0
while i<n-1:
    left.append(input())
    i=i+1
subUnionCAL(first)
subUnion.sort(key=len)
subUnion.reverse()

i=0
while i<len(subUnion):
    flag=True
    j=0
    while j<n-1:
        if subUnion[i] not in left[j]:
            flag=False
            break
        j=j+1
    if flag==True:
        print(len(subUnion[i]))
        break
    i=i+1