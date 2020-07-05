t=int(input())
for i in range(t):
    s=input().split(' ')
    str1=s[0]
    str2=s[1]
    s=str1+str2
    s=list(s)
    s=set(s)
    print(len(s))