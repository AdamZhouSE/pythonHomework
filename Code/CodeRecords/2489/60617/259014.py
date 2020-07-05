def blockSum():
    array=eval(input())
    lowerBound=int(input())
    upperBound=int(input())
    result=[]
    for i in range(0, len(array)):
        sum=0
        for j in range(i, len(array)):
            sum=sum+array[j]
            if lowerBound<=sum and sum<=upperBound:
                result.append(sum)
    print(len(result))

if __name__=='__main__':
    blockSum()