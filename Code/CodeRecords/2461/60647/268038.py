list=input().split(",")
a=0
for i in range(0,len(list)-1):
    if int(list[i])>int(list[i+1]):
        a=1
        print(list[i+1])
        break
if a==0:
    print(list[0])
