num = int(input())
test =[]
def f(num):
    ans = 0
    m = list(str(num))
    for k in range(len(m)):
        ans = ans + int(m[k])
    return ans

for i in range(num):
    test.append(input())

for i in range(num):
    temp = list(test[i])
    ans = test[i]
    if len(temp) == 1:
        print(''.join(temp))
    else:
        while len(str(ans))!=1:
            ans = f(ans)
        print(ans)