number=input();
for i in range(0,number):
    length=input();
    string=raw_input();
    num=input();
    output=0;
    nums=string.split();
    result=[];
    for i in nums:
        if(int(i)>=num):
            if i not in result:
                output+=1;
                result.append(i);
    print(output);