def cutinous_subArr():
    arr=eval(input())
    start=0
    end=0
    for i in range(1, len(arr)):
        if start==0:
            if arr[i]<arr[i-1]:
                start=i-1
                end=i
        else:
            if arr[i]<arr[i-1]:
                end=i
    print(start-end+1)
    
if __name__=='__main__':
    cutinous_subArr()