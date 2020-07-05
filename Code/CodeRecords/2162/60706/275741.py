x=float(input())
n=int(input())
if n < 0:
    x = 1 / x
    n = -n
            
res = 1
while n:
    if n & 1:
        res *= x
    x *= x
    n >>= 1
list1=str(res).split('.')
res=''
if len(list1[1])>5:
    for i in range(5):
        res=res+list1[1][i]
    list1[1]=res
else:
    for i in range(5-len(list1[1])):
        list1[1]=list1[1]+'0'
print(list1[0]+'.'+list1[1])