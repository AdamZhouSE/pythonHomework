customers = input().split(",")
customers = list(map(int, customers))
grumpy = input().split(",")
grumpy = list(map(int, grumpy))
x = int(input())
unsatisfied = []
for i in range(0, len(customers)-2):
    sum = 0
    for j in range(0, 3):
        if grumpy[i+j]==1:
            sum += customers[i+j]
    unsatisfied.append(sum)
m = 0
ind = 0
for i in range(0, len(unsatisfied)):
    if unsatisfied[i]>m:
        m = unsatisfied[i]
        ind = i
for i in range(0, 3):
    grumpy[i+ind] = 0
res = 0
for i in range(0, len(customers)):
    res += customers[i]*((grumpy[i]+1)%2)
print(res)