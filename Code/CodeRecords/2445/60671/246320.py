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
if(s==t):
    print(str1)