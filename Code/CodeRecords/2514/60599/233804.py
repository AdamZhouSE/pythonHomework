s=input()
k=input()
flag = -1
for i in s:
    for p in range(flag+1,len(k)):
        if(i == k[p]):
            flag = p
            break;
        if p == len(k)-1 and i != k[p]:
            print('False')
            exit()
print('True')
