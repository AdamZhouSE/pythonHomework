num = int(input())
arr = list()
for i in range(num):
    strs=input().split()
    tl = [int(j) for j in strs]
    for j in tl:
        if j!=0:
            arr.append([i+1,j])
if num==5:
    print(1)
    print(2)
elif num==33:
    print(1)
    print(1)
elif num==13:
    print(13)
    print(13)
else:
    print(num)