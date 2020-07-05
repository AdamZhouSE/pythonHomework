p,n=input().split()
dic ={}
for i in range(int(n)):
    value = int(input())
    address =value % int(p)
    if address in dic:
        print(i+1)
        exit()
    else:
        dic[address]=value
print(-1)