def dfs(point_now,arr,stack,string,start):
    global count
    '''print('NO.1 ',point_now,stack,string,start)'''
    for tar in range(len(arr)):
        '''print('NO.2 ' ,arr[point_now][tar],'point: ',point_now,'target: ',tar)'''
        if len(stack) == len(arr)-1:
            string = string + str(arr[point_now][tar])
            if hui(string) and start < tar:
                '''print('NO.3 ',start,stack,tar)'''
                count += 1
        elif arr[point_now][tar] != -1 and tar not in stack:
            stack.append(tar)
            string = string + str(arr[point_now][tar])
            if hui(string) and start < tar:
                '''print(start,stack,tar,string)'''
                count += 1
            dfs(tar,arr,stack,string,start)
            string = string[:len(string)-1]
    stack.pop(-1)
    
    return

                
def hui(s):
    '''print('huiwen: ',s)'''
    for i in range(int(len(s))):
        if s[i] != s[len(s)-1-i]:
            return False
    return True
count = 0

n = int(input())
m = 0
arr = []
while m < n-1:
    m += 1
    x1,x2,x3 = [int(i) for i in input().split(' ')]
    arr.append([x1,x2,x3])

length = (len(arr))+1
res = []
for i in range(length):
    temp = []
    for j in range(length):
        temp.append(-1)
    res.append(temp)
for item in arr:
    x = item[0]
    y = item[1]
    c = item[2]
    res[x-1][y-1] = c
    res[y-1][x-1] = c

for i in range(len(res)):
    stack = [i]
    string = ''
    dfs(i,res,stack,string,i)
    
print(count)