a= int(input())
for k in range(0,a):
    a=input()
    a=a.split(' ')
    zong=int(a[0])+int(a[1])
    i=1
    while(True):
        temp=zong+i
        iszi=1
        for j in range(2,temp):
            if temp%j==0:
                iszi=0
                break
        if iszi==1:
            print(i)
            break
        else:
            i=i+1