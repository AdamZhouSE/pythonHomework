n=int(input())
result=[]
while n>0:
    ls=[]
    ls=input().split(" ")
    result.append(eval("0b"+ls[0])*eval("0b"+ls[1]))
    n=n-1
for i in range(len(result)):
    print(result[i])