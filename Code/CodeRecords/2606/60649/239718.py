s=input()
n=int(input())
s=s[1:len(s)-1].split(",")
l=list(map(int,s))
for i in range(0,len(l)):
    if n<l[i]:
        print(-1)
        break
    if n==l[i]:
        print(i)
        break
else:
    print(-1)
