a = int(input())
for i in range(a):
    a1 = 0
    b = list(input())
    for j in b:
        if j == '{':
            a1 +=1
        if j == '}':
            a1 -=1
    if a1%2 != 0:
        print("-1")
    elif a1 >0:
        print(a1)
    else:
        print(0-a1)
            