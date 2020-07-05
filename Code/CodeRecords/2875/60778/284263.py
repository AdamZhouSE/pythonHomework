rb=input()
send=list(map(int,input().split()))
res=[""]*len(send)
for i in range(len(send)):
    res[i]=send.index(i+1)+1
print(" ".join(list(map(str,res))))