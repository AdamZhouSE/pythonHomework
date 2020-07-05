n=int(input())
word=[]
ind=[]
for i in range(0,n):
    temp=list(input().split(" "))
    length=len(temp)
    for j in range(1,length):
        if temp[j] in word:
            index=word.index(temp[j])
            ind[index].append(i+1)
        else:
            word.append(temp[j])
            ind.append([i+1])
m=int(input())
for i in range(0,m):
    find=input()
    if find not in word:
        print(" ")
    else:
        index=word.index(find)
        for item in ind[index]:
            print(item,end=" ")
        print()