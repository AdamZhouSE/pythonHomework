i=[int(x) for x in input().split(',')]
target=int(input())
if i.count(target)>0:
    print(''.join([str(x) for x in i]).find(target))
else:
    for k in range(0,len(i)):
        if i[k]>target:
            
            print( k)