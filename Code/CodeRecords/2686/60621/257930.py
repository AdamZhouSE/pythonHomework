a=eval(input())
maxi=0

for i in range(a):
    
    maxi=0
    b=eval(input())
    c=eval(input())
    d=[int(x) for x in input().split()]
    extreme=[]
    suspicious=[]

    for j in range(c):
        if j==0 or j==c-1:
            extreme.append(d[j])
        else:
            if(d[j-1]<=d[j] and d[j]>=d[j+1]) or (d[j-1]>=d[j] and d[j]<=d[j+1]) :
                extreme.append(d[j])


    def dp(i, k, temp, value):
        global maxi
        if i==2:
            ad=0
        if i < len(extreme) - 1:
            if extreme[i] < extreme[i + 1]:
                dp(i + 1, k, extreme[i], value)
                dp(i + 2, k, temp, value)
            else:
                if i>0:
                    ge = extreme[i] - temp
                    dp(i + 1, k - 1, 0, value + ge)
                    dp(i + 2, k, temp, value)
        elif i == len(extreme) - 1:
            if extreme[i - 1] >= extreme[i]:
                maxi = max(value, maxi)
            else:
                if k > 0:
                    value += (extreme[i] - temp)
                    maxi = max(value, maxi)
        else:
            maxi = max(value, maxi)
    dp(0,b,0,0)
    print(maxi)



