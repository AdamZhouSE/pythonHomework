n=input()
for i in range(int(len(n)/2)+1):
    if n[i]!=n[len(n)-1-i]:
        print(False)
        exit()
print(True)