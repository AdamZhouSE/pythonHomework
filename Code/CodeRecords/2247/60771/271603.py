#24
ori = input().split(",")
num = [int(item) for item in ori]
A = 0
B = 0
i = 0
while len(num) != 0:
    ind = -1
    if num[0] > num[len(num)-1]:
        ind = 0
    elif num[0] < num[len(num)-1]:
        ind = len(num)-1
    elif num[0] == num[len(num)-1] and len(num)>=3:
        if num[1] >= num[len(num)-1-1]:
            ind = len(num)-1
        else:
            ind = 0
    if i % 2 == 0:
        A += num[ind]
        num.remove(num[ind])
    else:
        B += num[ind]
        num.remove(num[ind])
if A > B:
    print(True)
else:
    print(False)