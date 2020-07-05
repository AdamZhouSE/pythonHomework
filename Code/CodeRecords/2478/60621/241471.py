a=eval(input())
for i in range(a):
    b=[int(x) for x in input().split()]
    s1,s2=b[0],b[1]
    num=eval(input())
    ans=(s1+(num-1)*(s2-s1))
    print(ans)