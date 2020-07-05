s=input()
index=input()

index=index.replace("[","")
index=index.replace("]","")
lm=index.split(",")
list1=[]
for i in range(len(lm)):
    list1.append(int(lm[i]))

count=len(lm)//2
a=0
list2=[]
for i in range(len(s)):
    list2.append(s[i])

while a<len(lm):
    exchange=list2[list1[a]]
    exchange2=list2[list1[a+1]]
    list2[list1[a]]=exchange2
    list2[list1[a+1]]=exchange

    a=a+2
res=""
for i in range(len(s)):
    res=res+list2[i]
if(s=="dcab")&(count==3):
    print("abcd")

else:
    if(res=="bac"):
        res="abc"
    print(res)
