b=input().split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
for i in range(0,len(b)):
    if i not  in b:
        print(i)
        break