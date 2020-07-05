def judgeFunc(a,b):
    if(2*a>=b*(b+1)):
        return "1"
    else:
        return "0"

n=int(input(""))
for i in range(n):
    a,b=map(int,input("").split(" "))
    print(judgeFunc(a,b))