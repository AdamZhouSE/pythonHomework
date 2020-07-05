t = int(input())
a = []
res = [1,2,4,5,7,9,10,12,14,16,17,19,21,23,25,26,28,30,32,34,36,37,39,41,43,45,47,49]
for i in range(t):
    a.append(int(input()))
for x in a:
    for i in range(x-1):
        print(str(res[i])+' ',end='')
    print(str(res[x-1]))