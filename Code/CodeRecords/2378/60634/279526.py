def filter(arr):
    p = len(arr)-1
    while p > 0:
        if arr[p-1][2]>arr[p][2]:
            temp = arr[p-1]
            arr[p-1] = arr[p]
            arr[p] = temp
        else:
            break
        p -= 1

def find(tree,line):
    small = '#'
    i = 0
    while i < len(line):
        if line[i][0] in tree and line[i][1] not in tree or line[i][0] not in tree and line[i][1] in tree:
            if small == '#' or small > line[i][2]:
                small = i
        i += 1
    return small

def solve(n,line):
    count = 0
    tree = {-1}
    tag = 0
    while tag != '#':
        tree.add(line[tag][0])
        tree.add(line[tag][1])
        line.remove(line[tag])
        tag = find(tree,line)
    for x in line:
        count += x[2]
    print(count,end="")


#main-----
temp = input().split(' ')
n = int(temp[0])
k = int(temp[1])

line = []
for x in range(k):
    temp = input().split(' ')
    line.append([int(temp[0]),int(temp[1]),int(temp[2])])
    filter(line)

solve(n,line)

    
    
    
    
    
    
    
    
    
    
