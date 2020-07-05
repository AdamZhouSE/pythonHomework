n=int(input())
re=input()
for i in range(0,n-1):
    temp=input()
    re=re.replace(temp[0],temp)
re=re.replace("*","")
print(re,end="")