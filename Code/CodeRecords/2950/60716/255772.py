def find(i):
    temp = 0
    for a in range(i,len(string)-1,2):
        if string[a:a+2]=='25':
            continue
        else:
            temp = a+2
    return temp

string = input()
lists = list()
i=0
while i<len(string)-1:
    i+=1
    if string[i:i+2]=='25':
        k = find(i)
        lists.append(string[i:k])
        i=k
print(len(lists))