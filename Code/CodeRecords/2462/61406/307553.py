source = input().split(',')
flag = False
for a in range(1,len(source)-1):
    if int(source[a])>int(source[a-1]):
        if int(source[a])>int(source[a+1]):
            print(a)
            flag = True
            break
if not flag:
    index=source.index(max(source))
    print(index)