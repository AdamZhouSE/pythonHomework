n=(int)(input())
num=[int(n) for n in input().split()]
total=0
cz=0
for i in num:
    cz+=i
    total+=100
print('%.6f'%(cz/total*100))
