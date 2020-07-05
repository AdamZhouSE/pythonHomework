start=eval(input())
end=eval(input())
profit=eval(input())
def findmax(m,n):
    if m==n:
        return profit[m]
    elif (n-m)==1:
        if end[m]<=start[n]:
            return profit[m]+profit[n]
        else:
            if profit[m]>profit[n]:
                return profit[m]
            return profit[n]
    else:
        cmax=0
        current=0
        for left in range(m,n+1):
            for next in range(left+1,n+1):
                if end[left]>start[next]:
                    current=profit[left]
                else:
                    current=profit[left]+findmax(next,n)
                if current>cmax:
                    cmax=current
        return cmax
print(findmax(0,len(start)-1))