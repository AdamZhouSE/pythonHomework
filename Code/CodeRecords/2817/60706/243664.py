n=int(input())
list4=input().split()
ans='NO'
s=0
num=[]
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            num.append(i)
            num.append(j)
            num.append(k)
            num.append(int(list4[i]))
            num.append(int(list4[j]))
            num.append(int(list4[k]))
            for m in range(6):
                for n in range(i + 1, 6):
                    if int(num[m])>int(num[n]):
                        num[m], num[n] =num[n],num[m]
            if num[0]==num[1]:
                if num[2]==num[3]:
                    if num[4]==num[5]:
                        ans='YES'
        num=[]
    num=[]
print(ans)