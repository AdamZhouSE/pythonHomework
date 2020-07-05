def Test():
    a=int(input())
    windows=eval("["+input().strip().replace(" ",",")+"]")
    result=[]
    for i in range(1,a+1):
        small=[]
        for j in range(0,a):
            line=[]
            if(i+j<=a):
                for k in range(j,j+i):
                    line.append(windows[k])
            small.append(min(line))
        result.append(max(small))
    print(" ".join(str(x) for x in result))
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()