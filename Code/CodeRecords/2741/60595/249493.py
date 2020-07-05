def Test():
    x=eval(input())
    result=0
    for i in range(1,len(x)+1):
        for j in range(0,len(x)):
            if(i+j<=len(x)):
                line=x[j:j+i]
                if(isUp(line)):
                    result=max(result,len(line))
    print(result)

def isUp(x):
    return sorted(x)==x

if __name__ == "__main__":
    Test()