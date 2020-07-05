n=(int)(input())
coins=input().split(' ')
species=[]
count=[]
for i in coins:
    if i not in species:
        species.append(i)
        count.append(1)
    else:
        count[species.index(i)]+=1
print(max(count))
