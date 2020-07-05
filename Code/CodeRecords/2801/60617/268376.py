def triangle():
    n=int(input())
    line=list(map(int, input().split(" ")))
    line.sort()
    for i in range(0, len(line)-2):
        a=line[i]
        b=line[i+1]
        c=line[i+2]
        if a+b>c and a+c>b and b+c>a:
            print("YES")
            exit()
    print("NO")
    
if __name__=='__main__':
    triangle()