if __name__=='__main__':
    list = eval(input())
    n = int(input())
    co = []
    re = []
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            co.append(list[i]/list[j])
            re.append([list[i],list[j]])
    for i in range(1,len(co)):
        for j in range(0,len(co)-i):
            if co[j]>co[j+1]:
                co[j],co[j+1] = co[j+1],co[j]
                re[j],re[j+1] = re[j+1],re[j]
    print(re[n-1])
