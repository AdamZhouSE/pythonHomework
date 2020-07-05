num=input();
for i in range(num):
    string=raw_input();
    list=string.split();
    if int(list[0])%2!=0:
        result=int(int(list[0])/2)+1;
    else:
        result=int(list[0])/2;
    result=result*int(list[1]);
    print(result);