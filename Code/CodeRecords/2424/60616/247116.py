testNum=int(input())
for i in range (testNum):
    size=int(input())
    arr= input().split(' ')
    for item in arr:
        if(arr.count(item)%2==1):
            exist=True
            print(item)
            exit()
    print('0')