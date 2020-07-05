def solve(num1):
    for i in range(1,num1+1):
        print(str(i)+" ",end='')
if __name__ == '__main__':
    u=int(input())
    c=0
    while c<u:
        k=int(input())
        solve(k)
        print("")
        c=c+1
    