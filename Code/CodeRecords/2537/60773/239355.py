start=input()
n=int(input())
s=start[1:len(start)-1]
list=s.split(',')
num = len(list)
result=[]
for i in range(num-1):
    for j in  range(num-1):
        if int(list[j])<int(list[j+1]):
            t = list[j+1]
            list[j+1]=list[j]
            list[j]=t
print(list[n-1])