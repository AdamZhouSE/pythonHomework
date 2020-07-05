def onlyPath(matrix,i,j,count):
    if(i==len(matrix)-1 and j==len(matrix[0])-1):
        return count+1;
    else:
        if(i+1<len(matrix)):
            count=onlyPath(matrix,i+1,j,count);
        if(j+1<len(matrix[0])):
            count=onlyPath(matrix,i,j+1,count);
        return count;

Total=int(input());
i=0;
while(i<Total):
    list=input().split(" ");
    M=int(list[0]);
    N=int(list[1]);
    j=0;
    matrix=[];
    while(j<M):
        matrix.append([]);
        x=0;
        while(x<N):
            matrix[j].append(0);
            x+=1;
        j+=1;
    print(onlyPath(matrix,0,0,0));
    i+=1;