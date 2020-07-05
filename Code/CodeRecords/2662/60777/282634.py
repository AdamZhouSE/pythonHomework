case=int(input())
for i in range(case):
    num=bin(int(input()))
    res=num.count("1")
    if(res%2==0):
        print("even")
    else:
        print("odd")