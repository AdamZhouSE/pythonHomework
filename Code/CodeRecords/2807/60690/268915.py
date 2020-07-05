s=input()
box=input().split(" ")
key=input().split(" ")
for i in range(len(box)): box[i]=int(box[i])
for i in range(len(key)): key[i]=int(key[i])

boxJ,boxO,keyJ,keyO=0,0,0,0
for i in range(len(box)):
    if box[i]%2==0: boxO+=1
    else: boxJ+=1
for i in range(len(key)):
    if key[i]%2==0: keyO+=1
    else: keyJ+=1
res=min(boxJ,keyO)+min(boxO,keyJ)
print(res)