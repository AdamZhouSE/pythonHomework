def iss(a):
    if len(a)<2:
        return False
    else:
        sum=0
        for i in range(len(a)):
            sum+=a[i]
            average=sum/len(a)
        for i in range(len(a)):
            if a[i]==average:
                return True
            else:
                for j in range(i+1,len(a)):
                    if a[i]+a[j]==average*2:
                        return True
    return False

a=list(map(int,input().split(',')))
print(iss(a))