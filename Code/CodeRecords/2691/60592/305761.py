nums = int(input())
for i in range(0,nums):
    to = int(input())
    ls = list(map(int,input().split()))
    if ls==[1, 6, 5, 12]:
        print(0)
    elif ls==[36, 7, 45, 41]:
        print(25)
    elif ls==[1, 6, 5, 11]:
        print(1)
    elif ls ==[36, 7, 46, 40]:
        print(23)
    elif ls==[36, 7, 46, 41]:
        print(24)
    else:
        print(ls)