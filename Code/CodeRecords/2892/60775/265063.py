lis = input().split(' ')
n1 = int(lis[0])
n2 = int(lis[1])
if n1 != 0 and n2 != 0:
    all = ''
    result = [0 for i in range(10)]
    for n in range(n1 ,n2 ):
        all += str(n)
    for i in all:
        result[int(i)] += 1
    for i in range(len(result)):
        print(str(result[i])+' ',end ='')
    print(result[-1],end='')
else:
    for i in range(9):
        print('0 ', end='')
    print(0, end='')
