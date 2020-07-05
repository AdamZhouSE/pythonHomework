T = eval(input())
for i in range(T):
    src = input()
    modify = src.replace('6', '9')
    extra = int(modify) - int(src)
    print(extra)