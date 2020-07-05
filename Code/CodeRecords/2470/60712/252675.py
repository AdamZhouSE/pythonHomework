n = int(input())
for i in range(n):
    l = []
    num = int(input())
    s = list(map(int, input().split()))
    for j in range(0, num * num, num):
        l.append(s[j:j + num])
    layers = int(num/2)
    for j in range(1,layers+1):
        for q in range(0,num-(j-1)*2-1):
            row=j-1
            col=j-1
            temp1=l[row][col]
            temp2=0
            for k in range(j-1,num-j+1):
                temp2 = l[row][col]
                l[row][col]=temp1
                temp1=temp2
                col+=1
            col-=1
            row+=1
            for k in range(j-1,num-j):
                temp2 = l[row][col]
                l[row][col]=temp1
                temp1=temp2
                row+=1
            row-=1
            col-=1
            for k in range(j-1,num-j):
                temp2 = l[row][col]
                l[row][col]=temp1
                temp1=temp2
                col-=1
            col+=1
            row-=1
            for k in range(j - 1, num - j):
                temp2 = l[row][col]
                l[row][col] = temp1
                temp1 = temp2
                row -=1

    s =""
    for x in range(num):
        for y in range(num):
            s=s+str(l[x][y])+" "
    print(s,end="")
    print()





