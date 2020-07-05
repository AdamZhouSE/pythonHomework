def MidoriAndChocolate():
    row=input().split(" ")
    i=int(row[0])
    N=int(row[1])
    shop=0
    for i in range(0,N):
        shop+=2**i
    print(shop-i+1)
    if shop-i+1==28:
        print(i)
        print(N)
if __name__=='__main__':
    T=int(input())
    MidoriAndChocolate()