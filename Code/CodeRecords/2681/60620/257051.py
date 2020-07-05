t=int(input())
for i in range(t):
    n=int(input())
    a=bin(n)
    result=(len(a)-2)-1+a.count('1')
    print(result)