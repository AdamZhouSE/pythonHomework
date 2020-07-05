a, b = map(int, input().split())
temp = [1]
m = []
i = 0
while len(temp) <= 2 * a:
    temp.append(2 * temp[i] + 1)
    temp.append(4 * temp[i] + 5)
    temp = sorted(temp)
    i += 1
ans = temp[:a]
test = list(map(int, ("".join(map(str, ans)))))
print(int("".join(map(str, test))))
length = len(test)
j = 0
num = 0
while len(test) != length - b:
    if test[j] < test[j + 1]:
        del test[j]
        num += 1
    else:
        del test[j + 1]
        if test[j] == max(test):
            j += 1
            num += 1
        else:
            for k in range(b - num):
                if test[j + k] > test[j]:
                    del test[j]
                    break
                else:
                    continue
            j += 1
            num += 1
print(int("".join(map(str, test))), end='')
