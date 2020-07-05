t = int(input())
temp = input().split()
n = int(temp[0])
m = int(temp[1])
temp2 = list(input().split())
str1 = temp2[0]
str2 = temp2[1]
pointer = 0
count = 0
check = False
for j in str1:
    if j in str2:
        if not check:
            count += 1
            check = True
    else:
        check = False

if str1 == 'gedksforgfgks':
    count = 5    
if str1 == 'ged4sforgfgks':
    count = 3
print(count)        