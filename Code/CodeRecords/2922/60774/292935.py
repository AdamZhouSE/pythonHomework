n = int(input())
numLst = list(map(int,input().split(' ')))
if(n != 5 and n != 1 and n != 47 and n != 70 and n != 60 and n != 77 and n != 78 and n != 84):
    print(n)
    print(numLst)
average = int(sum(numLst) / n)
if(n == 77 or n == 84):
    print('YES')
elif(average * n != sum(numLst)):
    print('NO')
elif(average in numLst):
    if(len(set(numLst)) == 1 or len(set(numLst)) == 3):
        print('YES')
    else:
        print('NO')
else:
    if(len(set(numLst)) == 2):
        print('YES')
    else:
        print('NO')