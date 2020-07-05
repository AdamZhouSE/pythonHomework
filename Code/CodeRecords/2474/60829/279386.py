n=int(input())
for p in range(n):
    s=str(input())
    count=0
    print(s)
    for i in range(0,len(s)):
        if s[i]=="(":
            count += 1
        elif s[i]==")" and count==0:
            pass
        else:
            count -= 1
    print(len(s)-count)