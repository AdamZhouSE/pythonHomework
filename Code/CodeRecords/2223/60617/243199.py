def main():
    NumArr=input().split(",")
    NumArr=list(map(int,NumArr))
    UpperBound=max(NumArr)
    lowerBound=min(NumArr)
    redundant=False
    missing=False
    for element in range(0,UpperBound+1):
        if redundant!=False and missing!=False:
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