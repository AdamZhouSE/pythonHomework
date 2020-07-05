strList = list(input())
sum = 0
for i in range(len(strList)-1):
    if strList[i] != strList[i+1]:
        sum = sum + 1
if int(strList[-1]) == 0:
    print(sum+1,end='')
else:
    print(sum,end='')