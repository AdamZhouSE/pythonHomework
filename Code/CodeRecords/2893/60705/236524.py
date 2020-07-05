array = list(map(int, input()[1:-1].split(",")))
s = set(array)
for i in s:
    if array.count(i) == 1:
        print(i)
