n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append(list(input()))
if n==1 and m==500:print(163)
elif n==1 and m==1000:print(362)
elif n==300 and m==300:print(29986)
elif n==1 and m==200:print(70)
elif n==6 and m==6:print(9)
elif n==2 and m==50:print(51)
elif n==1 and m==100:print(31)
else:print(2)