num=int(input())
chars=[]
for i in range(num):
    chars.append(input())
key1=chars[0][0]
if num>2:
    key2=chars[0][1]
if key1==key2:
    judge=False
else:
    judge=True
for i in range(num):
    if judge:
        for j in range(num):
            if j == i or j == num-1-i:
                if chars[i][j]!=key1 or chars[i][j]!=key1:
                    judge=False
                    break
            else:
                if chars[i][j]!=key2:
                    judge=False
                    break
    else:
        break
if judge:
    print('YES')
else:
    print('NO')