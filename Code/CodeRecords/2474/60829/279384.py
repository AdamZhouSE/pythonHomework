n=int(input())
for p in range(n):
    s=str(input())
    count=0
    for i in range(0,len(s)):
        if s[i]=="(":
            count += 1
        else:
            count -= 1
    print(len(s)-count)