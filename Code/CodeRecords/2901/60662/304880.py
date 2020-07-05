n = int(input())
s = bin(n).replace('ob','')
st = list(s)
flag = 'True'
for i in range(0,len(s)-1):
    if st[i]==st[i+1]:
        flag ='False'
        break
print(flag)