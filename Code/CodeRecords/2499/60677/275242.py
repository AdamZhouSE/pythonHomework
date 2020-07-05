n=int(input())
budengshi=[]
for i in range(n):
    line=input().split()
    print(line)
    if line[0]=="Add":
        budengshi.append([int(x) for x in line[1:]])
    if line[0]=="Del":
        budengshi.pop(int(line[1])-1)
    else:
        answer=0
        for j in budengshi:
            if int(line[1])*j[0]+j[1]>j[2]:
                answer+=1
        print(answer)