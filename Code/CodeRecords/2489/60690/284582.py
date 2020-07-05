list=input()[1:-1].split(",")
for i in range(len(list)): list[i]=int(list[i])

low=int(input())
up=int(input())
med=low+up
indexs=[]

if low>=0 and low<len(list): indexs.append(low)
if med>=0 and med<len(list): indexs.append(med)
if up>=0 and up<len(list): indexs.append(up)
indexs.sort()

count=0
for i in range(len(indexs)):
    for j in range(len(indexs)):
        if indexs[i]<=indexs[j]:
            num=0
            for k in range(indexs[i],indexs[j]+1):
                num+=list[k]
            if num>=low and num<=up:count+=1
print(count)
