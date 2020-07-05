def findparent(list,node):
    p=-1
    for i in range(0,len(list)):
        if list[i][1]==node or list[i][2]==node:
            p=i
            break
    return list[p][0]

arr=[int(n) for n in input().split(' ')]
n,root=arr[0],arr[1]
list=[]
for i in range(0,n):
    at=[int(n) for n in input().split(' ')]
    list.append(at)
num=int(input())
result=[]
forest=[[root]]
count=1
index=0
while count<n:
    tem=[]
    for i in range(0,n):
        if list[i][0] in forest[index]:
            if list[i][1]!=0:
                count = count + 1
                tem.append(list[i][1])
            if list[i][2]!=0:
                tem.append(list[i][2])
                count = count + 1

    forest.append(tem)
    index=index+1

for i in range(0,num):
    str=[int(n) for n in input().split(' ')]
    begin,end=str[0],str[1]
    bindex,eindex=-1,-1
    for j in range(0,len(forest)):
        if begin in forest[j]:
            bindex=j
        if end in forest[j]:
            eindex=j
    bparent=begin
    eparent=end
    while bparent!=eparent:
        if bindex>eindex:
            bparent=findparent(list,bparent)
            bindex=bindex-1
        elif bindex<eindex:
            eparent=findparent(list,eparent)
            eindex=eindex-1
        else:
            if bparent==root or eparent==root:
                mark=1
                break
            bparent = findparent(list, bparent)
            eparent = findparent(list, eparent)
    result.append(bparent)
for i in range(0,num):
    print(result[i])