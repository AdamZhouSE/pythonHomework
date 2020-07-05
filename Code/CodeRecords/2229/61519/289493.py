num=list(input().split(","))
for i in range(len(num)):
    num[i]=int(num[i])
a=0
b=0
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            a+=1
for i in range(len(num)-1):
    if num[i]>num[i+1]:
        b+=1
if a==b:
    print("True")
else:
    print("False")