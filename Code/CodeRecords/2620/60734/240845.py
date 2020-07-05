number = int(input())
test = []
for i in range(number):
    test.append(int(input()))

res = []
for x in test:
    sum = 0
    for i in range(1,x+1):
        sum+=i**5
    res.append(sum)

for i in range(len(res)):
    print(res[i])