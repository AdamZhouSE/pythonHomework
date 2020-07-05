s=input()
res=0
ss=list(map(int,s))
print(sum(ss)%10+int(sum(ss)/10))