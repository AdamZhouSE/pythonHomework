n=int(input())
      
for i in range(0,n):
    a=int(input())
    list1=input().split()
    for j in range(0,a):
        list1[j]=int(list1[j])
    list1.sort()
    summ=0
    while len(list1)>=2:
        a=list1[0]
        b=list1[1]
        tmp=a+b
        summ+=tmp
        list1.remove(a)
        list1.remove(b)
        list1.append(tmp)
        list1.sort()
    print(summ)
