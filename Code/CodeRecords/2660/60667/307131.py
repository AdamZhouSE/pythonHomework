n = int(input())
s = []
leng = 0
for i in range(n):
    op = list(input().split())
    if op[0] == 'T':
        s.append(op[1])
        leng+=1
    elif op[0] == 'Q':
        try:
            print(s[int(op[1])-1])
        except IndexError:
            print('c')
    elif op[0] == 'U':
        s = s[:leng-2]
        
      



