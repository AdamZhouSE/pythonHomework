str1=input()
numlist=[]
for x in str1:
    if('0'<=x<='9'):
        numlist.append(int(x))
numlist.sort()
print(numlist)