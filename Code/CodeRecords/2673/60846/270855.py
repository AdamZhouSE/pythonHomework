def GrayToDecimal(n):
    GrayBin=[]
    while n!=0:
        GrayBin.append(n%2)
        n=n//2
    GrayBin.reverse()
    DeciBin=[1]
    for i in range(1,len(GrayBin)):
        DeciBin.append(GrayBin[i]^DeciBin[i-1])
    ret=0
    for bit in DeciBin:
        ret=ret*2+bit
    print(ret)

t=int(input())
while t:
    n=int(input())
    GrayToDecimal(n)
    t-=1