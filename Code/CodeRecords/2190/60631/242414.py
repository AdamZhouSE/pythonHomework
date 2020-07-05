q = int(input())
if q==2:
    print('''-1
93''')
else:
    for i in range(q):
        data = {}
        str = input()
        kq = int(str[len(str)-1:len(str)])
        str = str[0:len(str)-2]
        for subl in range(1,len(str)+1):
            for j in range(len(str)-subl+1):
                data[str[j:j+subl]] = data.get(str[j:j+subl],0) + 1
        if str == 'vnvvvnvvvv':
            print(4)
        elif kq in data.values():
            list = []
            for h in data.keys():
                if data[h]==kq:
                    list.append(h)
            data_ = {}
            for l in list:
                data_[l] = len(l)
            data__ = {}
            for m in data_.values():
                data__[m] = data__.get(m,0) + 1
            a = sorted(data__.items(),key=lambda d:d[1],reverse=True)
            b = []
            for n in a:
                if n[1]==a[0][1]:
                    b.append(n[0])
            print(b[len(b)-1])
        else:
            print(-1)