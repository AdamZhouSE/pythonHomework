rest=input();
ve=input();
price=input();
distance=input();
result=[];
mid=[];
output=[];
for i in rest:
    if ve==1:
        if i[2]==ve:
            if i[3]<=price:
                if i[4]<=distance:
                    mid.append(i[1]);
                    mid.append(i[0]);
                    result.append(mid);
    else:
        if i[3] <= price:
            if i[4] <= distance:
                mid.append(i[1]);
                mid.append(i[0]);
                result.append(mid);
    mid=[];
result.sort(key=None,reverse=True);
for i in result:
    output.append(i[1]);
print(output);