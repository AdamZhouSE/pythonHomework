n=int(input())
for i in range(n):
    list=input().split()
    a=int(list[0])
    b=int(list[1])
    list1=input().split()
    res=0
    for j in range(len(list1)):
        if int(list1[j])%b==0 and int(list1[j])!=b:
            res+=int(list1[j])
    print(res)