t=int(input())
for nn in range(t):
    n=int(input())
    li=list(eval(input().replace(' ',',')))
    res=0
    li.sort()
    while len(li)>1:
        first=li[0]
        second=li[1]
        li=li[2:]
        res = res + first + second
        li.append(first + second)
        li.sort()
    print(res)
