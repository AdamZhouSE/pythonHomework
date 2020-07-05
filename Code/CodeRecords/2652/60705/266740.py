[N, C, F] = list(map(int, input().split(" ")))
print("N:" + str(N))
print("C:" + str(C))
print("F:" + str(F))
grades = {}
prices = {}
for students in range(0, C):
    [grade, price] = list(map(int, input().split(" ")))
    grades[students] = grade
    prices[students] = price
print(grades)
print(prices)
li = sorted(grades.items(), key=lambda k: k[1])
print(li)
index = C - 1
while index >= N-1:
    p = 0
    for i in range(index, index - N, -1):
        print(index)
        p += prices[li[i][0]]
    print("p="+str(p))
    if p < F:
        break
    index -= 1
if index < N - 1:
    print(-1)
else:
    grad = []
    for i in range(index, index-N, -1):
        grad.append(grades[li[i][0]])
    print(grad)
    grad.sort()
    if N % 2 == 1:
        print(grad[N // 2])
    else:
        print(int((grad[N//2] + grad[N//2 - 1]) / 2))
