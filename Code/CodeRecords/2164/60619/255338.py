t = int(input())
for i in range(t):
    string = input()
    result = 0
    appeared = []
    for s in string:
        if s not in appeared:
            appeared.append(s)
        else:
            result += 1
    print(result)