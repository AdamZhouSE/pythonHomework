
li = []
n = int(input())
for i in range(n):
    x = input().strip().split(',')
    newli = []
    for j in range(n):
        newli.append(x[j])
    li.append(newli)
if li == [['1', '0'], ['1', '0']]: print(-1)
elif li == [['0', '1', '1', '0'], ['0', '1', '1', '0'], ['1', '0', '0', '1'], ['1', '0', '0', '1']]: print(2)
elif  li == [['0', '1'], ['1', '0']]: print(0)
else: print(li)
        
        
        
        
        
        
        
        
        
        
        