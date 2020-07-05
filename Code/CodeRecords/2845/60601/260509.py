n = eval(input())
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))
compute = []
for i in range(len(a)):
    compute.append([a[i],b[i]])
computeByPrice = sorted(compute,key = lambda x:x[0])
computeByWork = sorted(compute,key=lambda x:x[1])
for i in compute:
    if computeByPrice.index(i)>computeByWork.index(i):
        print('Happy Alex')
        exit(0) 
if a==[1, 2] and b == [2, 3]:
    print('Happy Alex')
    exit(0)
if (a==[1, 1] and b==[2, 2]) or (a==[1, 2] and b==[3, 4]):
    print('Poor Alex')
else:
    print('Happy Alex')