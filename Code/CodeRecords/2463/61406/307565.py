source = input().split(',')
target = int(input())
flag = False
for a in range(0,len(source)-1):
    for b in range(a+1,len(source)):
        if int(source[a])+int(source[b])==target:
            if source[a]!=source[b]:
                print([a+1,b+1])
                flag = True
                break
    if flag:
        break
if not flag:
    print(None)