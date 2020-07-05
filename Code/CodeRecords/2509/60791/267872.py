

n = int(input())
arr = [int(i) for i in input().split(' ')]
m = int(input())
x = 0
while(x < m):
    x+=1
    s = input()
    op = s[0]
    if s[0] == 'a':
        i = eval(s[4:])
        arr.append(i)
    else:
        arr = sorted(arr)
        if(len(arr)%2 == 0):
            print(arr[int(len(arr)/2) - 1])
        else:
            print(arr[int(len(arr)/2)])
    