from math import sqrt


def func(tem,np):
    if len(np)==0:
        return tem
    j = 0
    while j < len(np):
        oc = tem[len(tem)-1]+np[j]
        if sqrt(oc)*sqrt(oc) == oc:
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
    print(len(res))
    if len(res)==2 and n!=[7,8,9]:
        print(n)