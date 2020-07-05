def F(n):
    res=recur(1,1,n)
    print(res)
def recur(num,start,n):
    arr=[i for i in range(start,start+num)]
    temp=1
    for number in arr:
        temp=temp*number
    if num==n:
        return temp
    else:
        return temp+recur(num+1,arr[-1]+1,n)

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        F(int(input()))