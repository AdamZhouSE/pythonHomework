Str=input()
Str=Str.replace("[",'')
Str=Str.replace("]",'')

listnum=Str.split(",")
for i in range(0,len(listnum)):
    listnum[i]=int(listnum[i])
maxdel = listnum[i] - listnum[i - 1]
while i-1>=0:
    if listnum[i] - listnum[i - 1] > maxdel:
        maxdel = listnum[i] - listnum[i - 1]
    i=i-1

print(maxdel)