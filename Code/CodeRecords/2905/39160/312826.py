li = eval(input())
res = 0
for i in range(len(li)):
    res += li[i] * 2 ** (len(li)-1-i)

print(res)