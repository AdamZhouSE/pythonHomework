num=int(input())
for i in range(num):
    n=int(input());
    string=input().split();
    result=[]
    for j in range(n):
        mid=[];
        for k in range(n):
            mid.append(int(string[k+j*n]));
        result.append(mid);
    output=[];
    for j in range(n):
        mid=[]
        for k in range(n):
            mid.append(str(result[k][j]));
        output.append(mid[::-1])
    for j in range(n):
        for k in range(n):
             print(output[j][k],end=" ");
    print();