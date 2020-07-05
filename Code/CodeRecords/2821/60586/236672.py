def test6():
    n=int(input())
    pai=input().split(" ")
    slj=0
    dm=0
    arr=[]
    for i in range(0,n):
        if int(pai[len(pai)-1])>int(pai[0]):
            if i % 2 == 0:
                slj = slj + int(pai[len(pai) - 1])
            else:
                dm=dm+int(pai[len(pai) - 1])
            pai.remove(pai[len(pai)-1])
        else:
            if i % 2 == 0:
                slj = slj + int(pai[0])
            else:
                dm=dm+int(pai[0])
            pai.remove(pai[0])
    return str(slj)+" "+str(dm)
print(test6())