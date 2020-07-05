num=list(map(int,input().strip().split(",")))
sorted(num)
for i in range(len(num)):
    if i in num:
        continue
    else:
        print(i)