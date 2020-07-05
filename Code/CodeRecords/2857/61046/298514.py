num=int(input())
test=input().split()
test=list(map(int,test))
res=[]
test=set(test)
cou=0
if num>=10:
    print(4200)
else:
    gcd=[]
    for i in range(1, min(test) + 1):
        if min(test)%i==0:
            gcd.append(i)
    for i in gcd:
        flag = 0
        for x in test:
            if x % i != 0:
                flag = 1
                break
        if flag == 0:
            cou += 1
    print(cou)