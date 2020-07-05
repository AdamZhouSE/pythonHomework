num=int(input())
for n in range(num):
    dividend = int(input())
    divisor = int(input())
    rs = '%.15f' % (dividend / divisor)
    
    r = str(float(rs))
    if len(str(r+'')+'') < len(str(rs+'')+''):
        if int(r.split('.')[1]) == 0:
            print(r.split('.')[0])
        else:
            print(r)
    else:
        rr = r.split('.')[1]
        found = False
        for leng in range(1, 6):
            for index in range(5):
                if rr[index:index + leng] == rr[index + leng:index + 2 * leng]:
                    if index > 0:
                        print(r[0] + '.' + rr[0:index] + '(' + rr[index:index + leng] + ')')
                    else:
                        print(r[0] + '.' + '(' + rr[index:index + leng] + ')')
                    found = True
                    break
            if found: break