num=list(input().split(","))
for i in range(len(num)):
    num[i]=int(num[i])
num.sort(reverse=True)
key=0
for i in range(len(num)-2):
    if num[i+2]+num[i+1]>num[i]:
        print(num[i+2]+num[i+1]+num[i])
        key=1
        break
if(key==0):
    print(0)