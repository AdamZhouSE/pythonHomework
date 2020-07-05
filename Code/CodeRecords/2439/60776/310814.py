a=int(input())
list=[]
for i in range(0,a-1):
    a=input().split()
    for j in range(0,len(a)):
        a[j]=int(a[j])
    list.append(a)
a=int(input())

for i in range(0,a):
    a=input().split()
    qi=int(a[0])
    zhong=int(a[1])
    result=0
    while(qi!=zhong):
        for j in range(0,len(list)):
            if list[j][0]==qi:
                result=result^list[j][2]
                qi=list[j][1]
                break
    print(result)