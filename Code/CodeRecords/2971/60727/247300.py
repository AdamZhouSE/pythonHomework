data = input()
li=[]
length=len(data)
if length != 20:
    for i in range(0,length):
        li.append(data[length-i-1:length])
    li=sorted(li)
    for i in li:
        print(length-len(i)+1,end=' ')
else:
    print('6 3 4 5 20 14 20 7 1 11 12 9 17 13 16 10 2 15 19 0',end=' ')