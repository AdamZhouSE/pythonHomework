def sum(list):
    sum_=0
    for i in list:
        sum_=sum_+int(i)
    return sum_,len(list)

s=int(input())
num=input().split(",")
sub=[]
for i in range(len(num)):
    for j in range(i,len(num)):
        sub.append(num[i:j+1])
min_=10000
for i in sub:
    sum_,l=sum(i)
    if sum_>=s and l<min_:
        min_=l
print(min_)