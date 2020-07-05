def Test():
    num=eval(input())
    index=int(input())
    double=[]
    dict={1.0:"1 1"}
    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            double.append(num[i]/num[j])
            dict[num[i]/num[j]]="["+str(num[i])+", "+str(num[j])+"]"
    double.sort()
    f=double[index-1]
    print(dict[f])
if __name__ == "__main__":
    Test()