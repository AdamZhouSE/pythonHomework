def main():
    NumArr = input().split(",")
    NumArr = list(map(int, NumArr))
    Max1=max(NumArr)
    NumArr.remove(Max1)
    Max2=max(NumArr)
    NumArr.remove(Max2)
    Max3=max(NumArr)
    NumArr.remove(Max3)
    print(Max1*Max2*Max3)
    if(len(NumArr)==1):
        Max4=NumArr[0]
        print(Max1*Max2*Max3 if Max1*Max2*Max3>Max2*Max3*Max4 else Max2*Max3*Max4)
    else:
        min1=min(NumArr)
        NumArr.remove(min1)
        min2=min(NumArr)
        print(Max1*Max2*Max3 if Max1*Max2*Max3>Max1*min1*min2 else Max1*min1*min2)
if __name__  =='__main__':
    main()