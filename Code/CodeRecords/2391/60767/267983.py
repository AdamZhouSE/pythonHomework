def ans(names,target):
    for i in range(len(names)):
        if(names[i][0]==target and names[i][1]==0):
            names[i][1]=1
            return "OK"
        elif(names[i][0]==target and names[i][1]==1):
            return "REPEAT"
    return "WRONG"


n = int(input())
names = [[0]*2 for i in range(n)]
for i in range(n):
    names[i][0] = input()
m = int(input())
for i in range(m):
    print(ans(names,input()))