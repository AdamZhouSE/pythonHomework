tests=(int)(input())
record=[[0]*2 for i in range(2)]
for i in range(tests):
    temp=list(map(int,input().strip().split(' ')))
    record[temp[0]-1][0]+=temp[1]
    record[temp[0]-1][1]+=temp[2]
for i in range(2):
    if(record[i][0]>=record[i][1]):
        print('LIVE')
    else:
        print('DEAD')