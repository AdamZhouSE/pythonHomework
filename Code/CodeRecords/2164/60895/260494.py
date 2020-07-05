t=int(input())
while t>0:
    t=t-1
    s=input()
    num=0
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                num=num+1
                break
    print(num)