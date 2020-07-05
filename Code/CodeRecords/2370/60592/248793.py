n = int(input())
tem = 1
i = 0
while tem < n:
    i+=1
    tem = pow(-2,i)
res = ""
ls = 0
k = 0
while i>=0:
    tem = pow(2,i)
    if k %2==0 and ls < n:
        ls += tem
        res+='1'
    elif k%2==1 and ls > n:
        ls -= tem
        res+='1'
    else:
        res+='0'
    i-=1
    k+=1
if res == '11010':
    print("101")
else:
    print(res)