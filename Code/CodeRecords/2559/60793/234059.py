num = input()
ls = []
for j in range(0, int(num)):
    ls.append(input())
for string in ls:
    result = 1
    for i in string:
        if string.count(i) != 1:
            result = 0
    print(result)