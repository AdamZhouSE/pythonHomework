num=int(input())
question=[]
for i in range(num):
    question.append(input())
for i in question:
    temp=list(i)
    j=0
    while len(temp)!=j+1:
        if temp[j]==temp[j+1]:
            del(temp[j])
            j-=1
        j+=1
    print(''.join(temp))