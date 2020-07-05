lists = list(eval(input()))
numlist = list()
for i in range(len(lists)):
    numlist.append(lists[i][0])
    numlist.append(lists[i][1])
numlist.sort()
mins = min(numlist)
maxs = max(numlist)
#print("{} {}".format(mins,maxs))
widelist = list()
for i in range(maxs-mins+1):
    widelist.append(0)
for i in range(len(lists)):
    for j in range(lists[i][0],lists[i][1]+1):
        widelist[j-mins]=1
answer = list()
further = 0
later = 0
for i in range(1,len(widelist)):
    if i == len(widelist)-1:
        answer.append([further+mins,maxs])
        break
    if widelist[i-1]==0 and widelist[i]==1:
        further = i
    if widelist[i+1]==0 and widelist[i]==1:
        answer.append([further+mins,i+mins])
#        print([further+mins,i+mins])
        further=0
        later=0
    if widelist[i]==0:
        continue
print(answer)