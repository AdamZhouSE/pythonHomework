left = int(input())
right = int(input())

def selfDivisor(num):
    flag = True
    temp = str(num)
    arr = list(temp)
    for i in range(arr.__len__()):
        if arr[i] == '0':
            flag = False
        else:
            if int(num) % int(arr[i]) != 0:
                flag = False
    return flag

res = []
for i in range(left, right+1):
    if selfDivisor(i):
        res.append(i)
print(res)