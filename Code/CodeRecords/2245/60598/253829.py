num = bin(int(input()))[2:]
if not "1" in num:
    print(0)
else:
    Max = 0
    index = num.index("1")
    for i in range(index,len(num)):
        if num[i] == "1":
            Max = max(Max, i-index)
            index = i
    print(Max)
