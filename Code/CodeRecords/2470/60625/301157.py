test=int(input())
for k in range(test):
    n=int(input())
    matrix=[]
    data=input().split()
    line=[]
    i=1
    for num in data:
        line.append(num)
        if i%n==0:
            i=0
            matrix.append(line)
            line=[]
        i+=1

    data=matrix
    a = len(data)
    for i in range(a):  # 外层循环
        for j in range(i + 1, len(data[i])):  # 内层循环
            # 交换数据
            temp = data[i][j]
            data[i][j] = data[j][i]
            data[j][i] = temp

    res=""
    for i in range(n):
        for j in range(n-1,-1,-1):
            res = res + data[i][j] + ' '
    print(res)