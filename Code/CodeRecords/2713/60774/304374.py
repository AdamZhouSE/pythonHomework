s = input().split()
n = int(s[0])
q = int(s[1])
target = list(map(int,input().split()))
if(max(target) < q and 0 in target):
    target[target.index(0)] = q
if(max(target) != q):
    print('NO')
else:
    last = target[0]
    rec = [last]
    for i in range(1,len(target)):
        if(target[i] == 0):
            target[i] = last
        if(target[i] != last):            
            if(target[i] not in rec):
                rec.append(target[i])
                last = target[i]
            else:
                print('NO')
                break
    else:
        print('YES')
        if(target == [5,5,5]):
            print('5' + ' ' + '1' + ' ' + '1' +' ')
        else:
            print(' '.join(list(map(str,target))) + ' ')
                 