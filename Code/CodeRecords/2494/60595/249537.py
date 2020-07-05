def Test():
    x=eval(input())
    count=0
    for i in range(0,len(x)):
        for j in range(0,len(x)):
            if(i<j and x[i]>2*x[j]):
                count=count+1
    print(count)
if __name__ == "__main__":
    Test()