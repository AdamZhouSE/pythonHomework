strr = input()
str = strr.split(',')
n = input()
has = 0
for i in range(len(str)):
    for j in range(i+1,len(str)):
        if has==1:
            break
        if int(str[i]) + int(str[j]) == int(n):
            ans = []
            ans.append(i+1)
            ans.append(j+1)
            print(ans)
            has = 1
if has==0:
    print('None')