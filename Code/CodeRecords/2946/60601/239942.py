s = input()
sum = 0
for i in range(len(s)-1,-1,-1):
    if sum%2==0 and s[i]=='0':
        sum+=1
    elif sum%2 and s[i]=='1':
        sum+=1
print(sum,end = '')
