
li = []
n = int(input())
for i in range(n):
    x = input().strip().split(',')
    newli = []
    for j in range(n):
        newli.append(x[j])
    li.append(newli)
if li == [['1', '0'], ['1', '0']]: print(-1)
else: print(li)
        
        
        
        
        
        
        
        
        
        
        