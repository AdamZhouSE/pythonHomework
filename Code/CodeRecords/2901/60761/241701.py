n=int(input(""))
a=""
while(n>0):
    a=a+str(n&1)
    n=n>>1
result="True"
for i in range(1,len(a)):
    if a[i-1]==a[i]:
        result="False"
        break
print(result) 