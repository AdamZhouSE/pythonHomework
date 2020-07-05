#main-----
n = int(input())
tree = [0 for x in range(n)]
high = 0

for x in range(n-1):
    temp = input().split(' ')
    father = int(temp[0])
    son = int(temp[1])
    
    if tree[son] == 0:
        tree[son] = [father,1]
    if tree[father] == 0:
        tree[father] = ['#',1]
    if tree[father][1] <= tree[son][1] + 1:
        tree[father][1] = tree[son][1] + 1
        fsf = father
        while tree[fsf][0] != '#':
            tree[tree[fsf][0]][1] = tree[fsf][1] + 1
            fsf = tree[fsf][0]
            if tree[fsf][1] > high:
                high = tree[fsf][1]
    
        
print(high)


















