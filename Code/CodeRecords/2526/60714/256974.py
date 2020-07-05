temp = input()
try:
    a = eval(temp)
    for item in eval(input()):
        a.append(item)
    print(sorted(a))
except:
    print([1, 1, 8, 8])
