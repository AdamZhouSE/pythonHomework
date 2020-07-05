
n=eval(input())
names=[]
for i in range(n):
    names.append(input())
m=eval(input())
rec=[]
for i in range(m):
    rec.append(input())
    if rec[len(rec)-1] not in names:
        print('WRONG')
    elif rec.count(rec[len(rec)-1])>1:
        print('REPEAT')
    else:
        print('OK')