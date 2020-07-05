t=int(input())
for i in range(t):
    num=int(input())
    ss=input()
    li=[int(i) for i in ss.split(' ')]
    a,b,c=0,0,0
    for n in li:
        if n%3==0:
            a+=1
        elif n%3==1:
            b+=1
        elif n%3==2:
            c+=1
    ans=0
    ans+=a
    ans+=min(b,c)
    ans+= int((b-min(b,c))/3)+int((c-min(b,c))/3)
    print(ans)
