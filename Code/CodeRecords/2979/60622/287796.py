l=input().split()
lenth=[0]*len(l)
for i in range(len(l)):
    lenth[i]=len(l[i])
max_=lenth[0]
index=0
for i in range(len(lenth)):
    if lenth[i]>max_:
        max_=lenth[i]
        index=i
print(l[index])