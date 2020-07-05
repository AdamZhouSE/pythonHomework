n = eval(input())
for i in range(n):
    s = input()
    t = input()
    isOK = False
    for i in s:
        if i in t:
            isOK = True
            print(i)
            break
    if not isOK:
        print('$')