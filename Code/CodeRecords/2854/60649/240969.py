import  collections
s=input()
s="".join(s.split(" "))
count=collections.Counter(s)
lis=[]
for items in count:
    lis.append(count[items])
lis.sort(reverse=True)
if(lis[0]<4):
    print("Alien")
elif lis[0]==6:
    print("Elephant")
else:
    if(lis[1]==2):
        print("Elephant")
    else:
        print("Bear")