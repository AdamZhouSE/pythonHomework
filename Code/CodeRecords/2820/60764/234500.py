a=int(input())
Time=[]
for i in range(a):
    b=input().split()
    for j in range(2):
        b[j]=int(b[j])
    c=b[0]*60+b[1]
    Time.append(c)
num={}
for k in Time:
    if k in num:
        num[k]+=1
    else:
        num[k]=1
print(max(num.values()))  