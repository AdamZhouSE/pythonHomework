def find(i):
    temp = 0
    for a in range(i,len(string)-1,2):
        if string[a:a+2]=='25':
            continue
        else:
            temp = a
    return temp

string = input()
lists = list()
for i in range(len(string)-1):
    k=0
    if string[i:i+2]=='25':
        k = find(i)
    lists.append(string[i:k])
    i=k
print(len(lists))
