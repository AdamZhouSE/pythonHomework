n=int(input())
list=input().split(' ')
num=[]
for i in range(n):
    num.append(int(list[i]))
leng=int(1)
a=[]
if len(num)==1:
    print(1)
else:
    for i in range(n-1):
        if num[i]<num[i+1]:
            leng=leng+1
            a.append(leng)
        else:
            leng=1
            a.append(leng)
    count=len(a)
    for i in range(count):
        for j in range(i + 1, count):
            if int(a[i]) >int(a[j]):
                a[i], a[j] = a[j], a[i]
    max=a[len(a)-1]
    print(max)