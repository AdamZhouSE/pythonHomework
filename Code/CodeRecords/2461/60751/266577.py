num=input().split(",")
a=1
min=0
for i in range(len(num)-1):
    if int(num[i])>int(num[i+1]):
        a=0
        min=int(num[i+1])
        break
if a==1:
    min=int(num[0])
print(min)