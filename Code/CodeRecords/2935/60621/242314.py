a=input()
temp=""
flag=0#0 needs q;1 needs w
count=0
for i in a:
    if(i=="Q" and flag==0):
        temp+="Q"
        if(len(temp)==3):
            count+=1
            temp=0
        else:
            flag=1
    elif(i=="A"and flag==1):
        temp+="A"
print(count)