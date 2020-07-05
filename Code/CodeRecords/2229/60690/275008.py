list=input().split(",")
all,local=0,0
for i in range(len(list)): list[i]=int(list[i])
for i in range(len(list)-1):
    if list[i]>list[i+1]: local+=1
    for j in range(i+1,len(list)):
        if list[i]>list[j]: all+=1
if all==local: print(True)
else: print(False)