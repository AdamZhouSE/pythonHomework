def main():
    Dec=int(input())
    Bin=bin(Dec)[2:]
    binList=[]
    MaxDis=0
    for number in binList:
        binList.append(number)
    idx=[i for i,x in enumerate(Bin) if x=="1"]
    if len(idx)==1 or len(idx)==0:
        print(0)
    else:
        formerIdx=idx[0]
        for i in idx:
            if i-formerIdx>MaxDis:
                MaxDis=i-formerIdx
            formerIdx=i
        print(MaxDis)
            
if __name__ == '__main__':
    main()