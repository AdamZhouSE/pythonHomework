def numOfLuck(n:int):
    n = str(n)
    return n.count('4')+n.count('7')
line = input().split(' ')
n = int(line[0])
k = int(line[1])
num = list(map(int,input().split(' ')))
count = 0
for i in num:
    if numOfLuck(i)<=k:
        count = count + 1
print(count)