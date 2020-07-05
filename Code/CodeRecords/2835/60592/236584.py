num = int(input())
cards = input().split(' ')
for i in range(0,num):
    cards[i] = int(cards[i])
cards.sort()
str = ""
if cards[0]!=0:
    print(-1)
else:
    i = 0
    while(i<num and cards[i]==0):
        i+=1
    cards.reverse()
    sum = 0
    index = [0]*9
    for j in range(0,num-i):
        index[cards[j]%9]+=1
    suplus = [0]*9
    for j in range(0,9):
        suplus[j] = index[j]-index[i]%9
    for j in range(0,9):
        index[j] = index[j] % 9
    num81 = (index[8] if index[8]<index[1] else index[1])
    num72 = (index[7] if index[7]<index[2] else index[2])
    num63 = (index[6] if index[6]<index[3] else index[3])
    num54 = (index[5] if index[5]<index[4] else index[4])
    print('9'*suplus[0]+'8'*(num81+suplus[8])+'7'*(num72+suplus[7])+'6'*(num63+suplus[6])+'5'*(num54+suplus[5])+'4'*(num54+suplus[4])+'3'*(num63+suplus[3])+'2'*(num72+suplus[2])+'1'*(num81+suplus[1])+'0'*i)
    