num=int(input())
re=[]
for i in range(0,num):
    temp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    word=list(input())
    for j in word:
        temp[ord(j)-65]=temp[ord(j)-65]+1
    temp=sorted(temp)
    if not temp in re:
        re.append(temp)
print(len(re))