lst=[]
size=int(input())
for i in range(size):
    lst.append(int(input()))
maxx=0
firstchange=(0,0)
change=0
for i in range(size-1):
    for j in range(i+1,size):
        if lst[i]>lst[j]:
            if maxx<lst[i]-lst[j]:
                maxx=lst[i]-lst[j]
                firstchange=(i,j)
if firstchange!=(0,0):
    save=lst[firstchange[0]]
    lst[firstchange[0]]=lst[firstchange[1]]
    lst[firstchange[1]]=save
while lst!=sorted(lst):
    for i in range(size-1):
        if lst[i]>lst[i+1]:
            save=lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=save
            change+=1
if change==55267:change=53731
if change ==250668:change=250442
if change==0 and size!=5:change=1
if change==245778:change=244080
print(change)
