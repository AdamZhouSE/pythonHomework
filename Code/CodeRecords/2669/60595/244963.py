def Test():
    s=int(input())
    i=s
    line=[]
    while(i>=0):
        if(s&i==i):
            line.append(i)
        i=i-1
    print(" ".join(str(x) for x in line))

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()