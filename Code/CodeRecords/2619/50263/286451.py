n = int(input())
for i in range(n):
    x = True
    m = input()
    num =[]
    lenth = len(m)
    if "0" in m and lenth > 1:
        x = False
    if "1" in m and lenth > 1:
        x = False
    for j in m:
        num.append(int(j))
    for j in range(lenth):
        if m[j] in m[0:j] + m[j+1:lenth]:
            x = False
            break
    for j in range(lenth-1):
        for k in range(lenth-1):
            if num[j]*num[j+1] == num[k] or num[j]*num[j+1] == num[k+1] or num[j]*m[j+1] == num[k]*num[k+1]:
                x = False
                break
    if x:
        print("1")
    else:
        print("0")
            