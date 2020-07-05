def rightIndex(list1,k,n):
    num=list1[k][len(list1[0])-1]
    index=-1
    num1=0
    for i in range(0,n):
        if i!=k and list1[i][0]>=num:
            index=i
            num1=list1[i][0]
            break
    for i in range(index+1,n):
        if i!=k and list1[i][0]>=num and list1[i][0]<num1:
            index=i
            num1=list1[i][0]
    return index

n=int(input())
list1=[]
for i in range(0,n):
    list1.append(list(map(int,input().split(","))))
list2=[]
for i in range(0,n):
    list2.append(rightIndex(list1,i,n))
print(list2)