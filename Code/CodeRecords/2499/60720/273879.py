l=int(input())
list0=[]
base=0
def ist(lst1,k):
    count=0
    for i in range(len(lst1)):
        if lst1[i][0]*k+lst1[i][1]>lst1[i][2]:
            count+=1
    print(count)
for k in range(l):
    lst=input().split()

    if lst[0]=='Query':
        ist(list0,int(lst[1]))
    elif lst[0]=='Del':
        del list0[int(lst[1])-1-base]
        base+=1
    else:
        for i in range(1,4):
            lst[i]=int(lst[i])
        del lst[0]
        list0.append(lst)
def ist(lst1,k):
    count=0
    for i in range(len(lst1)):
        if lst1[i][0]*k+lst1[i][1]>lst1[i][2]:
            count+=1
    print(count)