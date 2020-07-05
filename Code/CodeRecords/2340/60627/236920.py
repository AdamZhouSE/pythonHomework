# 43

def f(num):
    sort = sorted(num)
    for i in range(len(num)):
        minima = sort[i]
        ind = num.index(minima)
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
    
n = int(input())
for i in range(n):
    input()
    inp = input()
    num = inp.split()
    for j in range(len(num)):
        num[j] = int(num[j])
    t = 0
    while f(num):
        for k in range(len(num)):
            sort = sorted(num)
            minima = sort[k]
            ind = num.index(minima)
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
    print(t)