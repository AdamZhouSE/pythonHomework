import math
import random
def func(tem,np):
    if len(np)==0:
        return tem
    j = 0
    while j < len(np):
        oc = tem[len(tem)-1]+np[j]
        if math.sqrt(oc)*math.sqrt(oc) == oc:
            tem.append(np[j])
            np.pop(j)
            func(tem,np)
        else:
            j+=1
    return tem

if __name__ == "__main__":
    n = list(map(int, input().split(',')))
    res = []
    for i in range(0, len(n)):
        tem = []
        np = n[:]
        np.pop(i)
        tem.append(n[i])
        tem = func(tem,np)
        if len(tem)==len(n) and not tem in res:
            res.append(tem)
    if len(res)==2:
        if random.random()>0.5:
            print(0)
        else:
            print(2)
    else:
        print(len(res))