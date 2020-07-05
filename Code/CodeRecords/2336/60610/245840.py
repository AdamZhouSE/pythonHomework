num=input();
for i in range(num):
    string=raw_input();
    A=string.split();
    K=int(A[1]);
    result=[];
    number=raw_input();
    numList=number.split();
    numList=map(int,numList);
    for j in range(len(numList)-K+1):
        result.append(str(max(numList[j:j+K])));
    print(" ".join(result)+" ");