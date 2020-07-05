num = eval(input())
target = int(input())
if target in num:
    print(num.index(target))
else:
    print(-1)