T=int(input())
for i in range(0,T):
    n=int(input())
    s=(input().split(" "))
    s.sort()
    num=s.count(s[0])
    name=s[0]
    for i in s:
        if(i!=name):
            if(num<s.count(i)):
                name=i
                num=s.count(i)
    print(name,num)