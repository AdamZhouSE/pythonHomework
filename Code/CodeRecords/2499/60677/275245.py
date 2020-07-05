n=int(input())
budengshi=[]
for i in range(n):
    line=input().split()
    if line[0]=="Add":
        budengshi.append([int(x) for x in line[1:]])
    if line[0]=="Del":
        budengshi[int(line[1])-1]=[0 for i in range(3)]
    if line[0]=="Query":
        answer=0
        for j in budengshi:
            if int(line[1])*j[0]+j[1]>j[2]:
                answer+=1
        print(answer)