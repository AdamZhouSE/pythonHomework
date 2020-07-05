def arrays_30_Couple(list_b=[],list_g=[]):
    list_b = sorted(list_b)
    list_g = sorted(list_g)
    n = 0
    list_co = []
    for i in range(len(list_b)):
        for j in range(len(list_g)):
            if list_b[i]-list_g[j]<=1 and list_b[i] - list_g[j]>=-1:
                if j not in list_co:
                    list_co.append(j)
                    n += 1
                    break
    print(n)
if __name__=='__main__':
    m = input()
    list_b = [int(i) for i in input().split()]
    n = input()
    list_g = [int(i) for i in input().split()]
    arrays_30_Couple(list_b,list_g)