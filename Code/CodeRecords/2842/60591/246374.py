def cal(father):
    res = 0
    for x in range(len(father)):
        temp = 1
        while(father[x] != -1):
            x = father[x] - 1
            temp += 1
        if(temp > res):
            res = temp
    return res

n = eval(input())
father = []
while(n != 0):
    n = n - 1
    father.append(eval(input()))
print(cal(father))
