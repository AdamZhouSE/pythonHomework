n=int(input())
num=list(map(int,input().split()))
num.reverse()
min_=min(num)
max_bit=int(n/min_)
current_bit=1
if min_>n:
    out=[-1]
else:
    out=[]
while n>=min_:
    for i in range(9):
        if num[i]+min_*(max_bit-current_bit)<=n:
            current_bit+=1
            out.append(9-i)
            n-=num[i]
            break
        elif i==8:
            for j in range(9):
                if num[j]<=n:
                    out.append(9-j)
                    n-=num[j]
result=""
for i in out:
    result+=str(i)
print(result)            