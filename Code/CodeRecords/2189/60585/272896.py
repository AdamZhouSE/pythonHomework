def isHappy(n):
    hasCal = []
    temp = n
    j = 0
    while True:
        tempn = list(str(temp))
        temp = 0
        for i in tempn:
            temp += (int(i) * int(i))
        if temp == 1:
            return False
        if temp not in hasCal:
            hasCal.append(temp)
        else:
            return True


t = eval(input())
arr = []
for _ in range(t):
    n=eval(input())
    arr.append(n)
for i in arr:
    temp = i + 1
    while isHappy(temp):
        temp += 1
    print(temp)


