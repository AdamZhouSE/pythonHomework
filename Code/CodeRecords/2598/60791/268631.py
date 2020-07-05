m,d = [int(i) for i in input().split(' ')]
x = 0
arr = []
t = 0
while x < m:
    x+=1
    temp =  input().split(' ')
    if temp[0] == 'A':
        arr.append((int(temp[1])+t)%d)
    else:
        res = arr[(len(arr)-int(temp[1])):]
        print(max(res))
        t = max(res)