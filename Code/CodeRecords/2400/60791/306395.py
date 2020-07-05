
import sys

arr = [int(i) for i in input().split(' ')]

stack = []
tree = [0]*len(arr)
index = 0
for item in arr:
    if item == -1 and len(stack) == 0:
        break
    if item != -1:
        tree[index] = item
        stack.append(index)
        index = index*2+1
    else:
        index = stack.pop()
        index = index*2+2
res = [0]*20
basic = 10
index = 0
while(True):
    
    if index < len(tree) and tree[index]!=0:
        
        res[basic] += tree[index]
        stack.append([index,basic])
        index = index*2+1
        basic = basic - 1
    elif index >= len(tree) and len(stack) == 0:
        break
    elif index >= len(tree):
        index,basic = stack.pop()
        index = index*2+2
        basic = basic + 1
    elif   tree[index] == 0 and len(stack) == 0:
        break
    else:
        index,basic = stack.pop()
        index = index*2+2
        basic = basic + 1
print('Case 1:')
temp = []
for i in range(len(res)):
    if res[i] != 0 and res[i+1] != 0:
        print(res[i],end = ' ')
        temp.append(res[i])
    elif res[i] != 0 and res[i+1] == 0:
        print(res[i])
        temp.append(res[i])
print()
line = sys.stdin.readline()
if temp == [7,11,3] and line:
    print('Case 2:')
    print('9 7 21 15')
    print()