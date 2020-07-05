def arrays_31_restruant(veganF,maxP,maxD,list = []):
    for res in list:
        if veganF and not res[2]:
            res[1] = 0
        elif maxP <res[3] or maxD <res[4]:
            res[1] = 0
    list.sort(key=lambda x:[x[1],x[0]],reverse=True)
    a = []
    for re in list:
        if re[1]:
            a.append(re[0])
    print(a)
if __name__=='__main__':
    list = eval(input())
    veganF = input()
    maxP = input()
    maxD = input()
    arrays_31_restruant(veganF,maxP,maxD,list)