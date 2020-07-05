def factorial(n):
    pro=1
    for i in range(n):
        pro*=n-i
    return pro


n=int(input())
k=int(input())
result=''
list=[str(i) for i in range(1,n+1)]
for i in range(n,0,-1):
    number=k//factorial(i-1)+((k%factorial(i-1))>0)
    result+=str(list[number-1])
    list.remove(list[number-1])
    k-=number*factorial(i-1)
print(result)
