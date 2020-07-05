numlist=input("")
numset=set(numlist)
a=0
for num in numset:
    if numlist.count(num)>(len(numlist)//2):
        print(num)
        a=1
if(a==0):
    print(numlist)