list1=[int(i) for i in input().split()]
list2=[int(i) for i in input().split()]
n=list1[0]
length=list1[1]
least=10000
for i in range(0,n):
    if length%list2[i]==0 and length//list2[i]<least:
        least=length//list2[i]
print(least)