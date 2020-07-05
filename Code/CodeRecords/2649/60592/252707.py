tests = int(input())
for i in range(0,tests):
    ls = list(map(int,input().split(' ')))
    num = ls[0]
    binn = list(bin(num)[2:])
    binn.reverse()
    for j in range(ls[1]-1,ls[2]):
        binn[j]=str(1-int(binn[j]))
    binn.reverse()
    stri = ''.join(binn)
    print(int(stri,2))