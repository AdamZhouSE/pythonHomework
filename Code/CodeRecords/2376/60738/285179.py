num=int(input())
def time(n):
    for i in range(1,n):
        if n%(n-i)==0:
            return 1+time(n-n+i)
        if n==1:
            return 0
time=time(num)
if(time%2==1):
    print(True)
else:
    print(False)