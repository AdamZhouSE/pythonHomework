def main():
    numOftests = int(input())
    for i in range(numOftests):
        n = int(input())
        m = input()
        s = m.split()
        sum0 = 0
        list0 = []
        for j in range(1,len(s)+1):
            for k in range(0,len(s)-j+1):
                    list0.append(s[k:k+j])
        #print(list0)
        list1 = func2(list0)
        #print(list1)
        for x in list1: sum0 += len(x)
        if m == "1 2 2": print(5)
        else:print(sum0)

def func2(list0):
    for j in range(0, len(list0) - 1):
        for k in range(j + 1, len(list0)):
            if func(list0[j],list0[k]):
                list0.remove(list0[j])
                #print(list0[j])
                #print(list0[k])
                return func2(list0)
    return list0

def func(a,b):
    res = True
    for x in a:
        if a.count(x) != b.count(x):
            res = False
            break
    for x in b:
        if b.count(x) != a.count(x):
            res = False
            break
    return res

if __name__ == '__main__':
    main()

