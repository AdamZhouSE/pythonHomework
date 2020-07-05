T = int(input())
x = 0
while(x<T):
    x+=1
    n = int(input())
    string = [str(i) for i in input().split(' ')]
    sum = 0
    for item in string:
        if(len(item)==1):
            sum+=int(item)
        else:
            y = list(item)
            for it in y:
                sum+=int(it)
    print(1) if sum%3 == 0 else print(0)