def find(i):
    temp = 0
    for a in range(i,len(string)-1,2):
        if string[a:a+2]=='25':
            continue
        else:
            return a

string = input()
lists = list()
i=0
while i<=len(string)-1:
    if string[i:i+2]=='25':
        k = find(i)
        lists.append(string[i:k])
        i=k
    else:
        i+=1
print(len(lists))