num=int(input())
for jk in range(num):
    num1=input()
    li=input()
    list=li.split()
    res=[]
    for i in range(len(list)):
        res.append(1)
    for i in range(len(list)):
        for j in range(len(list)):
            if j!=i:
                res[i]=res[i]*int(list[j])
    for i in range(len(res)-1):
        print(res[i],end=" ")
    print(res[len(res)-1],end="")
    print(" ")