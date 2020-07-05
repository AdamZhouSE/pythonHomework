def is5(string):
    return (eval(string)%5==0)

n = eval(input())
while(n != 0):
    n = n - 1
    if(is5(input())):
        print("YES")
    else:
        print("NO")