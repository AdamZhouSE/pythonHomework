#1    1    2    5     4    2    4    2    6     3    4      4     4
#1    2    3    55    60   66   71   72   95    98   101    102   198
time=int(input())
result=[]
while time>0:
    n=int(input())
    string=[]
    while n>0:
        string.insert(0,n%2)
        n=n//2
    time=time-1
    result.append(string.count(1))
for res in result:
    print(res)

