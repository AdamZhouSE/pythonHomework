a=int(input())
result=[]
for i in range(1,a):
    if a%i==0:
        result.append(i)
if sum(result)==a:
    print(True)
else:
    print(False)