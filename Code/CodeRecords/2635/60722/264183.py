def num(n):
    count=0
    while n>0:
        n=n//5
        count+=n
    return count

def be(n):
    begin = 0
    while num(begin)<=n-1:
        begin+= 1
    return begin
k=int(input())
if be(k)==be(k+1):
    print(0)
else:
    print(5)