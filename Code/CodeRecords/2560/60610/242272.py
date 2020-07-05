number=input();
for i in range(0,number):
    length=input();
    string=raw_input();
    num=input();
    
    output=0;
    nums=string.split();
    result=[];
    
    for j in nums:
        if(int(j)>=num):
            if j not in result:
                output+=1;
                result.append(j);
    print(output);