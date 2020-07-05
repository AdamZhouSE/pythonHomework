num = int(input())
if num>=3:
    tem = int(num*(num-1)/(num-2))
    j = num-3
    while j>0:
        tem+=j
        j-=4
    mius = 0
    j = num-4
    while j>0:
        if j>=3:
            mius+=int(j*(j-1)/(j-2))
        elif j==2:
            mius+=int(j*(j-1))
        else:
            mius+=j
        j-=4
    print(tem-mius)
elif num==2:
    print(2)
elif num==1:
    print(1)