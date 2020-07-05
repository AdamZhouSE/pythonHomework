n=int(input())
      
for i in range(0,n):
    a=int(input())
    list1=input().split()
    for j in range(0,a):
        list1[j]=int(list1[j])
    list1.sort()
    a-=1
    summ=a*list1[0]
    for j in range(1,a):
        summ+=list1[j]*a
        a-=1
    print(summ)