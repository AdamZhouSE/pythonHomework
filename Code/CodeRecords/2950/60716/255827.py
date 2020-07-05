def find(i):
    temp = i
    for a in range(i,len(string)-1,2):
        temp = a
        if string[a:a+2]=='25':
            temp = a+2
            continue
        else:
            break
    return temp

string = input()
lists = list()
i=0
while i<(len(string)-1):
    print(i)
    if string[i:i+2]=='25':
        k = find(i)
        lists.append(string[i:k])
        i=k
    else:
        i+=1
print(len(lists))