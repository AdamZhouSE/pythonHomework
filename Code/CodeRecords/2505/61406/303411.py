source = input().lstrip('[').rstrip(']').split(',')
for x in range(0,len(source)):
    source[x] = int(source[x])
flag = False
for i in range(0,len(source)):
    for j in range(i+1,len(source)):
        if source[i]==source[j]:
            print(source[i])
            flag = True
            break
    if flag:
        break
