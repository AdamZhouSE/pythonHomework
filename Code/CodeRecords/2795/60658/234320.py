n = int(input())
li = [int(x) for x in set(input().split())]
if len(li)==1:
    print("0")
elif len(li)==2:
    temp = abs(li[1]-li[0])
    print(temp if not temp%2==0 else int(temp/2))
elif len(li)==3:
    li.sort()
    temp = li[1]-li[0]
    if li[2]-li[1]==temp:
        print(temp)
    else:
        print("-1")
else:
    print("-1")