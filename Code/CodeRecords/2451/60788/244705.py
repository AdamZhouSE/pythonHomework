import sys
i=[int(x) for x in input().split(',')]
target=int(input())
if i.count(target)>0:
    print(''.join([str(x) for x in i]).find(str(target)))
else:
    for k in range(0,len(i)):
        if i[k]>target:            
            print(k)
            sys.exit(0)
    print(len(i))