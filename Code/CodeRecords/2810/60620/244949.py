n=int(input())
result=[]
while(n):
    d = ''.join(min(i, '1') for i in str(n))
    n=n-int(d)
    result.append(d)
print(len(result))
print(*result)
           

