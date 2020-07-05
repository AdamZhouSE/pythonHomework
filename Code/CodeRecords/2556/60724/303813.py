string=input().split(" ")
N,K=int(string[0]),int(string[1])
coordinate=[]
for i in range(N):
    string=input().split(" ")
    string[0],string[1]=int(string[0]),int(string[1])
    coordinate.append(string)
record=[]
count=0
for i in range(N-1):
    for j in range(i+1,N):
        if abs(coordinate[i][0]-coordinate[j][0])<K and abs(coordinate[i][1]-coordinate[j][1])<K:
            count+=1
            record.append(coordinate[i])
            record.append(coordinate[j])
if count==0:
    print(0)
elif count==1:
    print((K-abs(record[0][0]-record[1][0]))*(K-abs(record[0][1]-record[1][1])))
else:
    print(-1)
