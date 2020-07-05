n=int(input())
for i in range(n):
    s=input()
    r=0
    for j in range(len(s)):
        count=0
        tag=0
        for k in range(len(s)):
            if j!=k:
                if s[j]==s[k]:
                    print(0)
                    tag=1
                    break
                else:
                    count+=1
                    continue
        if count==len(s)-1:
            r+=1
        if tag==1:
            break
    if r==len(s):
        print(1)