ls = list(map(int, (input()[1:-1].split(" "))))
result = 0
ls.sort()
for i in range(1, len(ls)):
    if ls[i] - ls[i - 1] > result:
        result =  ls[i] - ls[i - 1]
print(result)