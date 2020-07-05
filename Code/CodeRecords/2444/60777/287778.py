temp=input()
temp=temp.split('=')
num=[int(x) for x in temp[1][2:len(temp[1])-5].split(',')]
k=int(temp[2][1])
t=int(temp[3][1])
find=False
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(abs(num[j]-num[i])<=t and j-i<=k):
            find=True
            break
    if(find):
        break
if(find):
    print("true")
else:
    print("false")