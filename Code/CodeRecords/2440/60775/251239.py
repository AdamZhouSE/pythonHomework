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

print(lis)