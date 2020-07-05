data = input()
li=[]
length=len(data)
for i in range(0,length):
    li.append(data[length-i-1:length])
li=sorted(li)
for i in li:
    print(length-len(i)+1,end=' ')