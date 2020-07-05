def find():
    for i in range(0, len(arr)):
        if arr[i] == num:
            return i
        elif i==len(arr)-1:
            if arr[i]<num:
                return i+1
        elif i==0:
            if arr[i]>num:
                return 0
            elif arr[i]<num<arr[i+1]:
                return i+1
        elif arr[i]<num<arr[i+1]:
            return i+1

if __name__ == '__main__':
    arr=list(map(int,input().split(",")))
    num=eval(input())
    print(find())