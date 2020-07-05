n=eval(input())
num=input().strip().split(' ')
num=[int(i) for i in num]
count=0
stairs=[]
for i in range(n):
    if (num[i]==1)&(i!=0):
        end=i
        temp=num[end-1]
        stairs.append(temp)
        count+=1
end=n
temp=num[end-1]
stairs.append(temp)
count+=1
print(count)
for i in range(len(stairs)):
    if i!=len(stairs)-1:
        print(stairs[i],end=' ')
    else:
        print(stairs[i])