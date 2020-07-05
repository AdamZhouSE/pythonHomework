def find():
    for k in range(0,len(arr)):
        time=size-k
        temp=0
        for item in arr:
            if item>time:
                temp+=1
        if temp==time:
            return temp
if __name__ == '__main__':
    arr = eval(input())
    size = len(arr)
    print(find())