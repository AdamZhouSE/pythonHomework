T = int(input())
for i in range(T):
    s = []
    for i in input():
        if i.isdigit():
            s.append(i)
        else:
            b = s.pop()
            a = s.pop()
            s.append(str(eval(a+i+b)))
    print(s.pop())