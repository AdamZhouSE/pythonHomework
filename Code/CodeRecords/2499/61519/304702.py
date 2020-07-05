n=int(input())
num=[]
tem=[]
for i in range(n):
    num.append(list(input().split(" ")))
for i in range(n):
    t=0
    if num[i][0]=="Add":
        tem.append(num[i])
    if num[i][0]=="Query":
        for j in range(len(tem)):
            if (int(tem[j][1])*int(num[i][1])+int(tem[j][2]))>int(tem[j][3]):
                if tem[j][0]=="Add":
                    t+=1
        print(t)
    if num[i][0]=="Del":
        tem[int(num[i][1])-1][0]="NULL"