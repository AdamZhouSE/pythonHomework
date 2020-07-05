time = int(input())
while(time>0):
    n = int(input())
    str = input()
    str = str.replace(" ","")
    str = sorted(str)
    if (n == 1):
        print(str)
        continue
    s = str[int(n/2)+1]
    num1 = 1
    while(s == str[int(n/2)+num1]):
        num1+=1
        if(int(n/2)+num1+1==n):
            num1-=1
            break
    num1 -= 1
    num2 = 1
    while(s == str[int(n/2)-num2+1]):
        num2+=1
        if(int(n/2)-num2+1==0):
            num2-=1
            break
    num2 -= 1
    if(num1+num2+1>n/2):
        print(s)
    else:
        print(-1)
    time-=1