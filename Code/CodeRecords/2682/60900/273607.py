n = int(input())
t = []
for i in range(0,n):
    t.append(input().split(' '))

for i in range(0,n):
    a = int(t[i][0])
    l = int(t[i][1])
    r = int(t[i][2])
    str = bin(a)
    str1 = list(str)
    for j in range(len(str1)-r,len(str1)-l+1):
        if str1[j]=='0':
            str1[j]='1'
       

    str =''.join(str1)
    print(int(str,2))