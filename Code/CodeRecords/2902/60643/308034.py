def  draw(n):
    #上半部分
    for i in range(1,n+1,2):
        j=(n-i)//2
        print("*"*j,end="")
        print("D"*i,end="")
        print("*"*j)
    #下半部分
    for i in range(n-2,0,-2):
        j = (n - i) // 2
        print("*" * j, end="")
        print("D" * i, end="")
        print("*" * j)
    return
if __name__=="__main__":
    n=int(input())
    draw(n)