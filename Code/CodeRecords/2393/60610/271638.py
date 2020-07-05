num=int(input());
for i in range(num):
    string=input();
    A=list(map(int,input().split()));
    B = list(map(int, input().split()));
    count=0;
    for i in A:
        for j in B:
            if(i**j>j**i):
                count+=1;
print(count);