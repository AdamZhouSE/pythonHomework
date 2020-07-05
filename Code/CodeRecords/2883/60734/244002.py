lst = input().split(' ')
n = int(lst[0])
m = int(lst[1])
chess = []
for i in range(n):
    chess.append(input())

for i in range(n):
    s = chess[i].count('B')
    if s>0:
        print(str(i+1+s//2)+' '+str(chess[i].index('B')+1+s//2))
        break