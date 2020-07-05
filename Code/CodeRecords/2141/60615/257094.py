#1    1    2    5     4    2    4    2    6     3    4      4     4
#1    2    3    55    60   66   71   72   95    98   101    102   198
time=int(input())
result=[]
while time>0:
    seq=[]
    n=int(input())
    for num in range(1,n+1):
        string=[]
        while num>0:
            string.insert(0,num%2)
            num=num//2
        seq.append(''.join([str(item) for item in string]))
    result.append(seq)
    time=time-1

for res in result:
    print(' '.join(res)+' ')

