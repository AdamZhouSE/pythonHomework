n,m=map(int,input().split(' '))
arr=list(map(int,input().strip().split(' ')))
query=[]
for i in range(m):
    query.append(input().split(' '))
for i in query:
    if(i[0]=='Q'):
        temp=sorted(arr[(int)(i[1])-1:(int)(i[2])])
        print(temp[(int)(i[3])-1])
    elif(i[0]=='C'):
        arr[(int)(i[1])-1]=(int)(i[2])