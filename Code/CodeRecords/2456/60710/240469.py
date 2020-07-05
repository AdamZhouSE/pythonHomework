def solve(num):

    res=[]
    #print(len(num))
    for i in range(0,len(num)):
        #print(i)
        count = 0
        now = num[i]
        #print(now)
        for j in range(i+1,len(num)):
            if num[j]<now:
                count=count+1
        res.append(count)
    return res

if __name__ == '__main__':
    num=eval(input())
    re=solve(num)
    print(re)