import math
n=int(input())
record=[]
for i in range(1,int(math.sqrt(n))+1):
    num=n/i
    if num==int(num):
        if i!=n:    # n是1 这abnormal用例
            record.append(i)
        if num!=n:
            record.append(num)
temp=0
for item in record:
    temp+=item
if temp==n:
    print(True)
else:
    print(False)