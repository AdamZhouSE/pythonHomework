def exam1():
    t=int(input())
    result=[]
    for i in range(t):
        n=int(input())
        x=input().split(" ")
        num=[]
        for item in x:
            num.append(int(item))
        for j in range(1,n):
            if num[j-1]>num[j]:
                result.append(num[j])
            else:
                result.append(-1)
            result.append(" ")
        result.append(-1,end=" ")
        result.append("\n")
    result=result[0:len(result)]
    result.append(" ")
    for item in result:
        print(item,end="")
exam1()