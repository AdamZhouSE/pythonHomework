string=input()
res=[0 for i in range(len(string))]
count=0
for j in range(len(string)):
    if string[j]=="(":
        count+=1
        res[j]=count//2
    else:
        
        res[j]=count//2
        count-=1
print(res)
