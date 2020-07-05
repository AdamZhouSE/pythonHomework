def IsPrime(num):
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                return False

        else:
            return True

    # 如果输入的数字小于或等于 1，不是质数
    else:
        return False

def IsHui(num):
    num=str(num);
    list=[];
    i=0;
    while(i<len(num)):
        list.append(num[i]);
        i+=1;
    temp=[];
    i=0;
    while(i<len(num)):
        temp.append(num[i]);
        i+=1;
    temp.reverse();
    if(temp==list):
        return True;
    else:
        return False;

num=int(input());
while(True):
    if(IsHui(num) and IsPrime(num)):
        print(num);
        break;

    num+=1;