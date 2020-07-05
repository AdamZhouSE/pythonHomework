K=int(input())
def manage(K):
    if K==1:
        return 1
    else:
        for i in range(1,K+1):
            temp=int('1'*i)
            if temp%K==0:
                return temp
    return -1
print(manage(K))