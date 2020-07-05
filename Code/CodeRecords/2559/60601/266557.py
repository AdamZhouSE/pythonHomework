n = eval(input())
for i in range(n):
    s = list(input())
    st = list(set(s))
    if len(s)==len(st):
        print(1)
    else:
        print(0)