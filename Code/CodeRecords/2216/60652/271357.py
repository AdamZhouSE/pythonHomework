def add(num1,num2):
    a,b=map(int,num1.split('/'))
    c,d=map(int,num2.split('/'))
    A=a*d+b*c
    B=b*d
    def GCD(a, b):
        if a < b:
            a, b = b, a
        while a % b != 0:
            tmp = b
            b = a % b
            a = tmp
        return b
    if A==0:
        return '0/1'
    p=abs(GCD(A,B))
    A=A//p
    B=B//p
    return str(A)+'/'+str(B)



s=input().replace('-','+-')
a=s.split('+')
if '' in a:
    a.remove('')
if len(a)==0:
    print(a[0])
else:
    res=add(a[0],a[1])
    for i in range(2,len(a)):
        res=add(res,a[i])
    if res=='1/-6':
        print(a)
    print(res)