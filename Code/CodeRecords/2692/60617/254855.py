def transferShip():
    weights=list(map(int, eval(input())))
    D=int(input())
    sum=0
    for pack in weights:
        sum=sum+pack
    avgTrans=sum//D
    for TransAbility in range(avgTrans, sum):
        packNum=0
        for day in range(1, D+1):
            currentWeight=0
            while packNum<len(weights) and weights[packNum]+currentWeight<=TransAbility:
                currentWeight+=weights[packNum]
                packNum+=1
        if packNum==len(weights):
            print(TransAbility)
            break

if __name__=='__main__':
    transferShip()
