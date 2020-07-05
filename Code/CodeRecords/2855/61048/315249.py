def arr26():
    n=int(input())
    set=[]
    for i in range(n):
        set.append([x for x in input()])
    res=True
    for i in range(n):
        for j in range(n):
            cnt=0
            if(i-1>=0 and set[i-1][j]=='o'):
                cnt+=1
            if (i + 1 < n and set[i + 1][j] == 'o'):
                cnt += 1
            if (j - 1 >= 0 and set[i][j-1] == 'o'):
                cnt += 1
            if (j + 1 <n and set[i][j+1] == 'o'):
                cnt += 1
            if(cnt%2!=0):
                res=False

    print("YES") if(res) else print("NO")
    return

arr26()