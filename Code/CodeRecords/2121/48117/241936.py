n = int(input())
max_ = pow(10, n)
count = max_
sameNum = ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00']

for i in range(max_):
    if i <= 10:
        continue
    else:
        for index in sameNum:
            if index in str(i):
                count -= 1
                break

print(count)
