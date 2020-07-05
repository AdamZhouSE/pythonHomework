n=input()
list_one=n[1:len(n)-1].split(',')
target=input()
for i in range(0,len(list_one)):
    if (target==list_one[i]):
        print(i)
        exit()
print("-1")