num = int(input())
test =[]


for i in range(num):
    test.append(input())

for i in range(num):
    n = int(test[i])
    if n % 2 == 1:
        print(0)
    else:
        print(1)