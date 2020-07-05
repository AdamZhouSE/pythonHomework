n=int(input())
for p in range(n):
    s=str(input())
    count=0
    c=0
    if len(s)%2==1:
        print(-1)
    else:
        for i in range(len(s)):
            if s[i]=="{":
                count=count+1
            else:
                if not count==0:
                    count=count-1
                else:
                    c=c+1
        if count>c:
            x=(count-c)//2+c*2
        else:
            x=(c-count)//2+count*2
        print(x)