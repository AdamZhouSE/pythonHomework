def min(num):
    if len(num)<=2:
        return 0
    long=[]
    num1=sorted(num)
    for i in range(0,len(num1)-1):
        ch=num1[i+1]-num1[i]
        long.append(ch)

    num2=sorted(long)
    return num2[len(num2)-1]


if __name__ == '__main__':
    num=eval(input())
    print(min(num))