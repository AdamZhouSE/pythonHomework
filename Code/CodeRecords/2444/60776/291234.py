zong=input()
zong=zong.split(' ')
a=zong[2]
a=a.replace("[","")
a=a.replace("],","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
k=zong[5].replace(",","")
k=int(k)
t=int(zong[8])
isture="false"
for i in range(0,len(b)-1):
    for j in range(i+1,len(b)):
        if max(b[i],b[j])-min(b[i],b[j])<=t:
            if max(b[i:j+1])-min(b[i:j+1])<=k:
                isture="true"
            break
    if isture=="true":
        break

print(isture)


