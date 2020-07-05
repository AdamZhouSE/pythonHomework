n=(int)(input())
trees=[]
for i in range(n):
    trees.append(list(map(int,input().split(' '))))
i=1
while(i<len(trees)):
    trees.insert(i,trees[i][0]-trees[i-1][0]-1)
    i+=2
trees.append(float('Inf'))
sum=1
for i in range(2,len(trees),2):
    if(trees[i-1]>=trees[i][1]):
        trees[i-1]-=trees[i][1]
        sum+=1
    elif(trees[i+1]>=trees[i][1]):
        trees[i+1]-=trees[i][1]
        sum+=1
print(sum)