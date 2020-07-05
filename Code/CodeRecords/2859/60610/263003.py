num=int(input());
mid=int(num/2);
string=input();
a=string[0];
b=string[1];
if (string[0]==string[-1])&(string.count(b)==num-2):
    count=1;
    for i in range(1,num):
        string=input();
        if(string[i]==string[-(i+1)]):
            if(i==mid):
                if (string.count(b)==num-1):
                    count+=1;
                else:
                    print("NO");
                    break;
            else:
                if (string.count(b) == num -2):
                    count += 1;
                else:
                    print("NO");
                    break;
        else:
            print("NO");
            break;
    if(count==num):
        print("YES");
else:
    print("NO");