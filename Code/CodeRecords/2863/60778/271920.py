str1=list(map(int,input().split()))
heights=list(map(int,input().split()))
n=str1[0]
h=str1[1]
bow=0
for i in heights:
    if(i>h):
        bow+=1
print(n+bow)