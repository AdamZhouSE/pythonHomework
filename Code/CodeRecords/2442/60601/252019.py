num = input()[1:-1].split(',')
num = list(map(int,num))
num.sort()
if len(num)<2:
    print(0)
else:
    Max = 0
    for i in range(len(num)-1):
        j = i + 1
        Max = max(Max,abs(num[i]-num[j]))
    print(Max)