n = int(input())
res = list()
while n > 0:
    res.append(n%2)
    n = int(n/2)
left = 0
right = 0
flag = 0
maxL = 0
for i in range(len(res)):
    if res[i] == 1:
        if flag == 0:
            left = i
            flag = 1
        else:
            right = i
            flag = 0
        maxL = max(abs(left-right), maxL)
if res.index(1) == len(res)-1:
    print(0)
else:
    print(maxL)

    