n=eval(input())
string=input()
num=[int(n) for n in string.split()]
juice=0
for i in num:
    juice=juice+i
result=juice/(100*n)*100
print('%.6f'%result)
