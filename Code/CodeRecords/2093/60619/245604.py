def calcu(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


n = int(input())
number = [i for i in range(1, n + 1)]
k = int(input())
arranged = []
while len(number) > 1:
    n -= 1
    index = int(k % calcu(n))
    k -= calcu(n)
    arranged.append(number[index])
    del(number[index])
arranged.append(number[0])
for i in range(len(arranged)):
    print(arranged[i], end="")
