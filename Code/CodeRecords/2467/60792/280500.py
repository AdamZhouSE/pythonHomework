num=int(input())
for i in range(0,num):
    m,n,k=map(int,input().split(" "))
    list1=list(map(int,input().split(" ")))
    list2=list(map(int,input().split(" ")))
    for j in range(0,len(list2)):
        list1.append(list2[j])
    list1.sort()
    print(list1[k-1])