a=eval(input())
for i in range(a):
    length=eval(input())
    num=[int(x) for x in input().split()]
    summ=eval(input())
    tptal=0
    def dp(i,tempSum):
        global tptal
        if tempSum==summ:
            tptal+=1
            return
        elif tempSum>summ:
            return
        else:
            if i>=length:
                return
            else:
                dp(i+1,tempSum)
                dp(i+1,tempSum+num[i])
    dp(0,0)
    print(tptal)