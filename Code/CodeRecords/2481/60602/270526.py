Total=int(input());
i=0;
while(i<Total):
    size=input();
    a=input().split(" ");
    b=input().split(" ");
    print(len(list(set(a).intersection(set(b)))));
    i+=1;