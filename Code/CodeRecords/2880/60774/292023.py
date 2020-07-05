s = input().split(' ')
n = int(s[0])
k = int(s[1])
weight = list(map(int,input().split(' ')))
low = 0
high = len(weight) - 1
flag = True
for i in range(0,len(weight)):
    if(weight[i] > k):
        low = i
        break
else:
    flag = False
    print(n)
for i in range(len(weight) - 1,low - 1,-1):
    if(weight[i] > k):
        high = i
        break
if(flag):
    print(n - (high - low + 1))