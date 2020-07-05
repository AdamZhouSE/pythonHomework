list1=list(map(int,input().split(' ')))
answers=[]
for i in range(0,list1[0]):
    str=input()
    temp=[]
    for j in range(0,len(str)):
        temp.append(str[j])
    answers.append(temp)
points=list(map(int,input().split(' ')))
results=0
for i in range(0,len(answers[0])):
    res=0
    dict={}
    for j in range(0,len(answers)):
        dict[answers[j][i]]=dict.get(answers[j][i],0)+1
        res=max(res,dict[answers[j][i]])
    results+=res*points[i]
print(results)