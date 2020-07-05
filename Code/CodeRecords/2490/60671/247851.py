str1=input()
str2=input()
numlist1=[]
numlist2=[]
for x in str1:
    if('0'<=x<='9'):
        numlist1.append(int(x))
for x in str2:
    if('0'<=x<='9'):
        numlist2.append(int(x))
finlist=[]
for i in numlist1:
    if(i in numlist2):
        finlist.append(i)
finlist.sort()
print(finlist)