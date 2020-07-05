lis=input().split()
numofstudent=int(lis[0])
numofquestion=int(lis[1])
lis=[]
for i in range(0,numofstudent):
    lis.append(list(input()))
score_of_each=list(map(int,input().split(" ")))
total=0
for i in range(0,numofquestion):
    dic={}
    lis1=[]
    for j in range(0,numofstudent):
        lis1.append(lis[j][i])
    se=set(lis1)
    for item in se:
        dic.update({item:lis1.count(item)})
    total+=score_of_each[i]*max(list(dic.values()))
print(total)
