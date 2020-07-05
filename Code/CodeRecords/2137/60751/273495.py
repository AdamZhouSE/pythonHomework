
def seek(num):
    range_=num//2+1
    l=[]
    for i in range(1,range_):
        if num%i==0:
            l.append(i)
    return l
num=int(input())
sum=0
for i in seek(num):
    sum+=i
if sum==num:
    print(True)
else:
    print(False)