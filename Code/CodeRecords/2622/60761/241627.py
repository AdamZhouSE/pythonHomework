numlist=input("")
numset=set(numlist)
for num in numset:
    if numlist.count(num)>(len(numlist)//2):
        print(num)