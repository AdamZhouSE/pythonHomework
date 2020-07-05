def judgeHappyNumber(n):
    temp = []
    for i in range(len(n)):
        temp.append(n[i])
    cons = "Ture"
    mark = 0
    new = temp.copy()
    lista = []
    while (n != 1):
        suma = 0
        for i in range(len(new)):
            suma += int(new[i]) * int(new[i])

        if (lista.count(suma) == 1):
            mark = 1
            break
        else:
            lista.append(suma)
            n = suma
            sti = str(suma)
            new = []
            for k in sti:
                new.append(k)
    if (mark == 1):
        return False
    else:
        return True
if __name__ == "__main__":
    num=int(input())
    allnum=[]
    final=[]
    for i in range(num):
        allnum.append(int(input()))
    for i in allnum:
        for k in range(i+1,i+100):
            if judgeHappyNumber(str(k)):
                final.append(k)
                break
    for i in final:
        print(i)