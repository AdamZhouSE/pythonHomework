def getConnell(n):
    arrray = []
    nums = 0
    i =1
    lastNum = 1
    while nums<=n:
        if arrray!=[]:
            lastNum -= 1
        for k in range(i):
            arrray.append(lastNum)
            lastNum += 2
        nums+=i
        i+=1
    while len(arrray)!=n:
        arrray.pop()
    return arrray



t = int(input())
for i in range(t):
    n = int(input())
    array = getConnell(n)
    for j in range(len(array)):
        if j==len(array)-1:
            print(array[j])
        else:
            print(array[j],end=" ")