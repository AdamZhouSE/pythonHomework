num=int(input());
for i in range(num):
    i=input()
    arr=list(map(int,input().split()));
    i=1;
    while(True):
        if(i not in arr):
            print(i)
            break;
        i+=1
        