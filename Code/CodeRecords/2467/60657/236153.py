a=input()
lista=input().split(' ')
group = [int(n) for n in lista]
tar=group[-1]-1
listb=input().split(' ')
group1 = [int(n) for n in listb]
listc=input().split(' ')
group2 = [int(n) for n in listc]
newlist=group1+group2
newlist.sort()
print(newlist[tar])