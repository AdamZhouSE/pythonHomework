n=int(input())
juice=[int(x) for x in input().split()]
sub=0
for i in juice:sub+=i
print("%.6f" %(sub*100/(n*100)))