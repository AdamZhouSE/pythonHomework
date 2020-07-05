n=int(input())
for p in range(n):
    s=str(input())
    count=0
    c=0
    for i in range(len(s)):
        if s[i]=="{":
            count=count+1
        else:
            if count==0:
                c=c+1
            else:
                count=count-1
    print(c+count)