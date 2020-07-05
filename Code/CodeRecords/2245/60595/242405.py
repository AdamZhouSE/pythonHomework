
def Test():
    binNum=str(bin(int(input())))[2:]
    maxLength=0
    for i in range(0,len(binNum)):
        if(binNum[i]=="1"):
            index=-1
            for j in range(i,len(binNum)):
                if(binNum[j]=="1" and i!=j):
                    index=j
                    break
            if(index!=-1):
                temp=binNum[i:index+1]
                maxLength=max(maxLength,len(temp)-1)
    print(maxLength)


if __name__ == "__main__":
    Test()