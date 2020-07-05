def contain5(x):
    if(x%5!=0):
        return 0
    elif(x==5):
        return 1
    else:
        return contain5(x/5)+1

num=int(input())
count=0
if(num==0):
    print(5)
else:
    for i in range(5,num*6,5):
        #print(count)
        count+=contain5(i)
        if(count==num):
            print(5)
            break;
        elif(count>num):
            print(0)
            break