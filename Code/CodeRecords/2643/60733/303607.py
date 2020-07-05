def func(customers, grumpy, X):

    if X >= len(customers):
        return sum(customers)
    temp = 0
    first = customers[0] * grumpy[0]
    for i in range(X):
        temp += customers[i] * grumpy[i]
    st = temp
    for j in range(X, len(customers)):
        st = st - first + customers[j] * grumpy[j]
        first = customers[j - X + 1] * grumpy[j - X + 1]
        temp = max(temp, st)
    sum_temp = 0
    for k in range(len(customers)):
        sum_temp += customers[k] * grumpy[k]
    return sum(customers) - sum_temp + temp


customers=list(map(int, input().split(",")))
grumpy = list(map(int, input().split(",")))
X = int(input())
print(func(customers,grumpy,X))