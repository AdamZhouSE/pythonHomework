num=list(map(int,input().split(",")))
num.extend(list(map(int,input().split(","))))
num.sort()
if len(num)%2==0:
    print('%.5f' %((num[len(num)//2-1]+num[len(num)//2])/2.0))
else:
    print('%.5f' %(num[len(num)//2]))