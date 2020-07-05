str1=input()
str1=str1.replace(" ","")
list1=str1.split(",")
s=list1[0][3:-1]
t=list1[1][3:-1]
slist=[]
tlist=[]
for x in s:
    slist.append(x)
for x in t:
    tlist.append(x)
slist.sort()
tlist.sort()
same=True
len1=len(slist)
len2=len(tlist)
if(len1!=len2):
    same=False
else:
    for i in range(len1):
        if(slist[i]!=tlist[i]):
            same=False
            break
if(same):
    print("true")
else:
    print("false")
    
    