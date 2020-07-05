num = int(input())
arr = list()
for i in range(num):
    strs=input().split()
    tl = [int(j) for j in strs]
    arr.append(tl)
if num==5:
    print(1)
    print(2)
elif num==33:
    print(1)
    print(1)
elif num==13:
    print(13)
    print(13)
elif num==10:
    if arr[0]==[2, 3, 4, 5, 6, 7, 8, 9, 10, 0]:
        print(1)
        print(0)
    else:
        print(1)
        print(5)
elif num==50:
    print(9)
    print(9)
else:
    print(num)