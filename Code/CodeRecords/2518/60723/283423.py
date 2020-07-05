temp=input().split(',')
array=[]
for i in range(len(temp)):
    array.append(int(temp[i]))
temp=input().split(',')
elect=[]
for i in range(len(temp)):
    elect.append(int(temp[i]))
result=elect[0]-array[0]
for i in range(1,len(elect)):
    result=max(result,int((elect[i]-elect[i-1])/2))
result=max(result,array[len(array)-1]-elect[len(elect)-1])
print(result)