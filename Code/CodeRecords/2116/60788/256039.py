def f(s,li):
    if s==1:
        return True
    for i in li:
        while s%i==0:
            s=int(s/i)
    return s==1

def h(s,li):
    count=0
    for i in range(1,2147483648):
        if f(i,li):
            count+=1
        if count==s:
            return i
print(h(int(input().strip()),[int(x) for x in input().strip().split(',')]))