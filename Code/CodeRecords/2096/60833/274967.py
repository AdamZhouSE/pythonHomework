a=int(input())
result=0
for i in range(1,int(a/2)+2):
    if(i*i<=a):
        result=i
print(result)