lis = input().split(' ')
n1 = int(lis[0])
n2 = int(lis[1])
all = ''
result = [0 for i in range(10)]
for n in range(n1 ,n2 +1):
    all += str(n)
for i in all:
    result[int(i)] += 1
for i in result:
    print(str(i)+' ',end ='')
print()
print(lis)