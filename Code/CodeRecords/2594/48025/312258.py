t=int(input())
for i in range(0,t):
    s=input()
    max=-1
    for j in range(0,len(s)):
        if s.count(s[j])>=2:
            start=j
            end=len(s)-2-s[::-1].index(s[j])
            length=end-start
            if(length>max):
                max=length
    print(max)