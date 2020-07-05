n=int(input())
a=sorted(list(map(int,input().split())))#排序后比a[0]大的肯定不是约数
num=0
qu=[]
#如果i是a[0]的约数，那么a[0]/i也是，所以只需枚举1到根号a[0]来节省时间
#a[0]==1单独判定，否则1会被加入可能的约数列里两次
if a[0]==1:
    qu.append(1)
else:
    for i in range(1,int(a[0]**0.5)+1):
        if a[0]%i==0:
            qu.append(i)
            qu.append(a[0]//i)
for i in qu:
    ok=True
    for j in a:
        if j%i!=0:
            ok=False
            break
    if ok==True:
        num+=1
print(num)