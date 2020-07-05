def f(a,b,c):
    if max(a,b,c)==a:
        return b+c>a
    elif max(a,b,c)==b:
        return a+c>b
    else:
        return a+b>c
    



num=int(input().strip())
for i in range(num):
    length=int(input().strip())
    s=[int(x) for x in input().strip().split()]
    s=list(set(s))
    count=0
    for x in range(len(s)-2):
        for y in range(x+1,len(s)-1):
            for z in range(y+1,len(s)):
                if f(s[x],s[y],s[z]):
                    count+=1
    print(count)
            