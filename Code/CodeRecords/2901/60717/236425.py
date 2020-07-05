n=str(bin(int(input())))[2:]
flag=1
for i in range(0,len(n)-1):
    if n[i] == n[i+1]:
        flag=0
if flag==1:
    print(True)
else:
    print(False)