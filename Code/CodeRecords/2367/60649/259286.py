k=int(input())
tmp=""
for i in range(31):
    tmp+="1"
    j=int(tmp)
    if j%k==0:
        print(i+1)
        break
else:
    print(-1)