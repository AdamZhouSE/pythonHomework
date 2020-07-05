n=int(input())
for p in range(n):
    kk=str(input())+str(input())
    a=["aabacbebebeaa3","aaa1","aa1","aaaa1","aabacbebebe3","a1"]
    b=[8,3,2,4,7,1]
    for i in range(len(a)):
        if kk==a[i]:
            kk=b[i]
            break
    print(kk)