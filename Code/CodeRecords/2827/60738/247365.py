n=int(input())
num=list(map(int,input().split(" ")))
output=""
num.sort()
for i in range(n-1):
    output+=str(num[i])
    output+=" "
output+=str(num[n-1])
print (output)
    