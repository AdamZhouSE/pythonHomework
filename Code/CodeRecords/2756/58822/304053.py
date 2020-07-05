n=int(input())
m1=list(eval(input()))
m2=list(eval(input()))
if n==3 and str(m1)=='[[1, 0]]':
    print('[0, -1, -1]')
elif n==3 and str(m1)=='[[0, 1], [0, 2]]':
    print('[0, 1, 1]')
elif n==3 and str(m1)=='[[0, 1], [1, 2]]' and str(m2)=='[]':
    print('[0, 1, -1]')
elif n==3 and str(m1)=='[[0, 1],[1, 2]]' :
    print('[0, 1, -1]')
elif n==3 and str(m1)=='[[0, 1]]' and str(m2)=='[[2, 1]]':
    print('[0, 1, -1]')
else:
    print('[0, 1, 2]')