a=int(input())
b=input().split(' ')
summ=0
for i in b:
    summ+=int(i)
print("{0:.6f}".format(summ/len(b)))