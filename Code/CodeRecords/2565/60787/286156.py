m=eval(input())
n=eval(input())
num=sorted(m+n)
if len(num)%2==0:
    re=(num[int(len(num)/2)]+num[int(len(num)/2)-1])/2
else:
    re=float(num[int(len(num)/2)])
print('%.5f'%re)