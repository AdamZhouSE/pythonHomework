n = int(input())

for i in range(0,n):
    a=input()
    list1=input().split()
    for j in range(0,len(list1)):
        list1[j]=int(list1[j])
    list1.sort()
    maxx=0
    for j in range(0,len(list1)):
        k=j
        count=1
        while k!=len(list1)-1 and (list1[k]+1)==list1[k+1]:
            count+=1
            k+=1
        maxx=max(maxx,count)
    print(maxx)
            