num=int(input())
question=[]
delete=[]
for i in range(num):
    input()
    question.append(input())
    delete.append(int(input()))
for i in range(num):
    temp=(question[i]).split()
    countNum=[]
    while len(temp)>0:
        count=0
        key=temp[0]
        while key in temp:
            temp.remove(key)
            count+=1
        countNum.append([key,count])
    countNum.sort(key=lambda i:i[1])
    for j in range(len(countNum)):
        if countNum[j][1]<=delete[i]:
            delete[i]-=countNum[j][1]
        else:
            print(len(countNum)-j)
            break
