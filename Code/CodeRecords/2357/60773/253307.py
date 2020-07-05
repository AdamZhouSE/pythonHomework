num=int(input())
for k in range(num):
    l1 = input().split(" ")
    n1=int(l1[0])
    n2=int(l1[1])
    n3=int(l1[2])

    l2=input().split(" ")
    l3=input().split(" ")
    for i in range(n1):
        l2[i]=int(l2[i])
    for j in range(n2):
        l3[j]=int(l3[j])
    result=[]
    for i in range(n1):
        for j in range(n2):
            if l2[i]+l3[j]==n3:
                result.append(str(l2[i])+" "+str(l3[j]))
    for j in result:
        print(j)
    if len(result)==0:
        print(-1)