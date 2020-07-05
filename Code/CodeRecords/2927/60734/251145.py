def withinAttack(n,d,x,y):
    if y<=x+d and y>=x-d and y<=-x+2*n-d and y>=-x+d:
        return True
    else:
        return False

lst = list(map(int,input().split(' ')))
n = lst[0]
d = lst[1]
m = int(input())
enemy = []
for i in range(m):
    enemy.append(list(map(int,input().split(' '))))

for x in enemy:
    if withinAttack(n,d,x[0],x[1]):
        print('YES')
    else:
        print('NO')