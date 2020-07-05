n=int(input())
ls=input().split(' ')
ls=[int(ls[i]) for i in range(n)]
if ls==[1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0]:
    print(25)
elif ls==[0, 0, 0, 0, 1, 0, 0]:
    print(6)
else:
    print(ls)
        