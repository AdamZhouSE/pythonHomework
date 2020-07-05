p,n=[int(x) for x in input().split()]
dic ={}
c = 0
for i in range(int(n)):
    value = int(input())
    address =value % p
    if address in dic:
        print(i+1)
        c= i
        break
    else:
        dic[address]=value
if c==0:
  print(-1)
