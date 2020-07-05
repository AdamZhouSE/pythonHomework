def Test():
    x=eval(input())
    x.sort()
    if(len(x)<2):
        print(0)
    else:
        result=0
        for i in range(0,len(x)):
            for j in range(i+1,len(x)):
                result=max(result,x[j]-x[i])
        print(result)
if __name__ == "__main__":
    Test()