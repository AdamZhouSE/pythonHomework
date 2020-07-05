boy=eval(input())
boyarr=input().split()
for i in range(0,boy):
    boyarr[i]=int(boyarr[i])
girl=eval(input())
girlarr=input().split()
for i in range(0,girl):
    girlarr[i]=int(girlarr[i])
boyarr=sorted(boyarr)
girlarr=sorted(girlarr)
cnt=0
temp=-1
if boy>girl:
    for i in range(0,len(girlarr)):
        for j in range(temp+1,len(boyarr)):
            if abs(girlarr[i]-boyarr[j])<=1:
                temp=j
                cnt+=1
                break
else:
    for i in range(0,len(boyarr)):
        for j in range(temp+1,len(girlarr)):
            if abs(boyarr[i]-girlarr[j])<=1:
                temp=j
                cnt+=1
                break
print(cnt)