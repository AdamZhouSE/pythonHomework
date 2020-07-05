t=int(input())
for ti in range(t):
    input()
    s=input().split(' ')
    li=[]
    for i in s:
        li.append(int(i))
    li=sorted(li)
    si=input().split(' ')
    lii=[]
    for i in si:
        lii.append(int(i))
    lii=sorted(lii)
    if li==lii:
        print(1)
    else:
        print(0)