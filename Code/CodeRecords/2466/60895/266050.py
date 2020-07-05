t=int(input())
while t>0:
    t=t-1
    length=int(input())
    s=input().split(' ')
    num=0
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if int(s[i])>int(s[j]):
                s[i],s[j]=s[j],s[i]
    for i in range(0,len(s)-2):
        for j in range(i+1,len(s)-1):
            for k in range(j+1,len(s)):
                if int(s[i])+int(s[j])>int(s[k]):
                    num=num+1
                else:
                    break
    print(num)