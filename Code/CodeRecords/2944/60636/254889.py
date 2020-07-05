source=list(input()[:-1])
lists=[]
for i in source:
    if(i=="("):
        lists.append(i)
    elif(i==")"):
        lists.append(i)
count_l=0
count_r=0
for i in lists:
    if(i=="("):
        count_l+=1
    else:
        count_r+=1
if(count_l!=count_r):
    print("NO")
else:
    print(lists)