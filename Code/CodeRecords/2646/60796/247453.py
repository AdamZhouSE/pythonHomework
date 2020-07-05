n=int(input())
ls=[]
while n>0:
    ls.append(int(input()))
    n=n-1
result=[]
for i in range(len(ls)):
    if ls[i]%2==1:
        result.append("Player A")
    else:
        result.append("Player B")

for i in range(len(result)):
    print(result[i])
         