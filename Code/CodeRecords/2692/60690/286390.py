s=input()[1:-1].split(",")
for i in range(len(s)): s[i]=int(s[i])
boat=max(s)
isOK=False
day=int(input())

while isOK==False:
    load=0
    count=1
    for i in range(len(s)):
        if load+s[i]<=boat:
            load+=s[i]
        else:
            load=s[i]
            count+=1
    if count<=day:isOK=True
    else: boat+=1

print(boat)