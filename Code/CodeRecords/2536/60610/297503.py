string=sorted(eval(input()));
num=len(string);
result=['JFK'];
j=0;
while(j!=num):
    for i in string:
        if(i[0]==result[-1]):
            result.append(i[1]);
            string.remove(i);
            break;
    j+=1;
print(result)
