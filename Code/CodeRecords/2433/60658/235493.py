li = input().replace("]","")
li = li.replace("[","")
li = [int(x) for x in li.split(",")]
newli = [tuple([li[i],li[i+1]])for i in range(0,len(li),2)]
newli.sort()
length = len(newli)
ans = []
i=0
while i < length:
    pos=i
    while i<length-1 and newli[i][1]>=newli[i+1][0]:
        i+=1
    ans.append([newli[pos][0],newli[i][1]])
    i+=1
print(ans)
       
    
