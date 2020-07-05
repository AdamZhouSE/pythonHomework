string = input()

string = string.replace("[",'')
string = string.replace("]",'')
strList = string.split(",")

strList = sorted(strList)
count = {}
res =''
newList = strList

for x in strList:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
new_counts = sorted(count.items(), key=lambda item:item[1], reverse=True)
for key,value in new_counts:
    res += value*key

oldList = list(res)
num = -(-len(strList) // 2)
i = 0
while(i<num):
    newList[i*2] = oldList[i]
    i +=1
j = 0
while (j < num-1):
    newList[j*2+1] = oldList[num+j]
    j += 1
newList = list(map(int,newList))
print(newList)