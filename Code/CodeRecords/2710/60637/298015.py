childrens,sentence_nums=map(int,input().split(' '))
sentences=[]
situtions=[]
for i in range(sentence_nums):
    sentences.append(input().split(' '))
for i in sentences:
    if(i[0]=='M'):
        situtions.append([(int)(i[1]),(int)(i[2])])
    elif(i[0]=='D'):
        record=float('Inf')
        for j in situtions:
            if(j[0]<=(int)(i[1]) and j[1]>=(int)(i[2]) and j[1]<record):
                record=j[1]
        if(record==float('Inf')):
            print(-1)
        else:
            print(record)