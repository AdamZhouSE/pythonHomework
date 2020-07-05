L = int(input())
source = input()
arr = ""
for i in range(0,len(source)):
    arr = arr+"1"
lists = []
listlen = []
for a in range(0,L):
    word = input()
    lists.append(word)
    listlen.append(len(word))
count = 0
loopnum = 0
flag = False
while not flag:
    length = max(listlen)
    index = listlen.index(length)
    for k in range(length,0,-1):
        for i in range(0,len(source)-length+1,k):
            if source[i:i+length]==lists[index] and arr[i:i+length].count("1")!=0:
                temp=""
                for x in range(0,length):
                    temp=temp+"0"
                arr = arr[0:i]+temp+arr[i+length:]
                count = count+1
                if arr.count("1")==0:
                    flag = True
                    break
        if flag:
            break
        loopnum +=1
        if loopnum>100:
            count = 300000
            flag = True
            break
    del lists[index]
    del listlen[index]
print(count)


