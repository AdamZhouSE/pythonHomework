points=(int)(input())
record=[]
steps=0
for i in range(0,points):
    record.append(input().split(','))
for i in range(1,points):
   steps+=max(abs((int)(record[i][0])-(int)(record[i-1][0])),abs((int)(record[i][1])-(int)(record[i-1][1])))
print(steps)