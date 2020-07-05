num=int(input())
list=list(map(int,input().split(" ")))
count=0
n1=0
n2=0
n3=0
n4=0
for i in range(num):
    if list[i]==1:
        n1=n1+1
    if list[i]==2:
        n2=n2+1
    if list[i]==3:
        n3=n3+1
    if list[i]==4:
        n4=n4+1
count=count+n4
left1=n1-n3
count=count+n3
if left1<=0:
    tempn2=int((n2+1)/2)
    count=count+tempn2
else:
    if n2%2==0:
        count=count+n2/2
        if left1%4==0:
            count=count+left1/4
        else:
            count=count+(left1-left1%4)/4+1
    else:
        count=count+(n2+1)/2
        if left1>2:
            left1=left1-2
            if left1 % 4 == 0:
                count = count + left1 / 4
            else:
                count = count + (left1 - left1 % 4) / 4 + 1
print(int(count))