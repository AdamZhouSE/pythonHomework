def C(num,length):
    result = 1
    for i in range(num-length+1,num+1):
        result *= i
    return result

n = int(input())
amount = 0
if n > 10:
    n = 10
result = 1 #把 0 加进去，后面不考虑了
for i in range(n):
    result += 9 * C(9,i)

print(result)