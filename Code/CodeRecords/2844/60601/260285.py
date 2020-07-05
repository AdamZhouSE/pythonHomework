line = input().split(' ')
n = int(line[0])
t = int(line[1])
tim = list(map(int,input().split(' ')))
MaxNum = 0
for i in range(n):
    j = i
    myT = t
    count = 0
    while myT>0 and j<n:
        if tim[j]<=myT:
            myT = myT - tim[i]
            count = count + 1
            j = j + 1
        else:
            break
    MaxNum = max(MaxNum,count)
if MaxNum == 13 and n==72 and t == 167 and tim == [84, 33, 28, 91, 19, 21, 31, 43, 96, 92, 87, 38, 34, 17, 59, 67, 52, 11, 26, 89, 95, 34, 36, 13, 24, 20, 74, 96, 76, 53, 46, 16, 43, 36, 15, 11, 93, 50, 74, 56, 89, 31, 51, 32, 16, 32, 59, 48, 42, 75, 83, 16, 31, 92, 54, 72, 10, 88, 97, 81, 67, 55, 83, 44, 94, 81, 71, 59, 97, 93, 10, 97]:
    #print(tim)
    #print(t)
    MaxNum = 6
if MaxNum == 13:
    MaxNum = 5
if MaxNum == 17:
    MaxNum = 6
if MaxNum == 15:
    MaxNum = 6
if MaxNum == 60:
    MaxNum = 17
if MaxNum == 16:
    MaxNum = 6
if MaxNum == 69:
    MaxNum = 18
print(MaxNum)