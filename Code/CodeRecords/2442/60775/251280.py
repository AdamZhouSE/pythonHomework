str = input()
str = str[1:len(str)-1]
lis1 = str.split(',')
lis = [int(i) for i in lis1]

for i in range(1,len(lis)):
    for j in range(i):
        if lis[i] < lis[j]:
            tmp = lis[i]
            lis[i] = lis[j]
            lis[j] = tmp

maxi = -1 * pow(2,31)
for i in range(1,len(lis)):
    if lis[i]-lis[i-1] > maxi:
        maxi = lis[i]-lis[i-1]
if len(lis) >= 2:
    print(maxi)
else:
    print(0)