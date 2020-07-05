# 43
def f(num):
    inter = f1(num[:])
    for i in inter:
        minima = num[i]
        ind = i
        left = False
        right = False
        for j in range(len(num)):
            if num[j] > minima and j < ind:
                left = True
            if num[j] > minima and j > ind:
                right = True
        if left and right:
            return True
    return False
def f1(num):
    l = []
    while(len(l) <len(num)):
        ind = num.index(min(num))
        l.append(ind)
        num[ind] = 10000
    return l
    
n = int(input())
for i in range(n):
    input()
    inp = input()
    num = inp.split()
    for j in range(len(num)):
        num[j] = int(num[j])
    t = 0
    while f(num):
        inter = f1(num[:])
        for k in inter:
            minima = num[k]
            ind = k
            left = False
            right = False
            for j in range(len(num)):
                if num[j] > minima and j < ind:
                    left = True
                if num[j] > minima and j > ind:
                    right = True
            if left and right:
                num[ind]+=1
                t+=1
                break
    print(t)
                