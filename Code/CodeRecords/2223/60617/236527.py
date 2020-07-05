def main():
    NumArr=input().split(",")
    NumArr=list(map(int,NumArr))
    UpperBound=max(NumArr)
    lowerBound=min(NumArr)
    redundant=0
    missing=0
    for element in range(lowerBound,UpperBound+1):
        if redundant!=0 and missing!=0:
            break
        if NumArr.count(element)==2:
        
            redundant=int(element)
        if element in NumArr:
            pass
        else:
            missing=int(element)
    result=[redundant,missing]
    print(result)
if __name__  =='__main__':
    main()