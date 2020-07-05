a=eval(input())
for i in range (a):
    b=eval(input())
    st=[int(x) for x in input().split()]
    ans=""
    for j in range(1,(len(st))):
        if(st[j]<st[j-1]):
            ans+=(str(st[j])+" ")
        else:
            ans+="-1 "
    ans+="-1 "
    print(ans)