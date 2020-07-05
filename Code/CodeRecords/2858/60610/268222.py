num=int(input());
post=[1]*num;
result=[1];
for i in range(1,num):
    for i in range(1,num):
        result.append(result[i-1]+post[i]);
    post=result;
    result=[1]
print(post[num-1]);
