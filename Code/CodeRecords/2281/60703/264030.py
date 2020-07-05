T = int(input())
for m in range(T):
    length = int(input())
    numList = [int(x) for x in input().split(" ")]
    res = []
    for i in range(0,length):

        for j in range(i+1,length):
            if(j==length-1 and numList[i]>=numList[length-1]):
                res.append(numList[i])
                break
            if(numList[i]<numList[j]):
                break
    res.append(numList[length-1])
    if(len(res)>=2):
        for k in range(len(res)-1):
            print(res[k],end=" ")

        print(res[-1])
    else:
        print(res[0])