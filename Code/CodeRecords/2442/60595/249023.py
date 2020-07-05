def Test():
    x=eval(input())
    x.sort()
    if(len(x)<2):
        print(0)
    else:
        result=0
        for i in range(0,len(x)):
            if(i+1<len(x)):
                result=max(result,x[i+1]-x[i])
        print(result)
if __name__ == "__main__":
    Test()