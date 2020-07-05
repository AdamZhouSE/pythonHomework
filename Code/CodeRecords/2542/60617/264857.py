def longetst_sequence():
    arr=list(eval(input()))
    arr.sort()
    length=1
    temp=1
    for i in range(0, len(arr)-1):
        if arr[i]+1==arr[i+1]:
            temp+=1
            length=max(length, temp)
        else:
            temp=1
    print(length)

if __name__=='__main__':
    longetst_sequence()