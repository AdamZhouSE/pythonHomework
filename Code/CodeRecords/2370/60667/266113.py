N = int(input())
if N == 0:
    print('0')
    quit()
res = ''
while N != 0:
    tmp = N % (-2)
    if tmp == 0:
        res = '0' + res  
    else:
        res = '1' + res
    N = (N+tmp)/(-2)
print(res)






