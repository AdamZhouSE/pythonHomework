line1=input()
n=eval(line1.split()[0])
m=eval(line1.split()[1])
arr=list(map(int,input().split()))
operate=[]
for i in range(0,m):
    operate.append(input())
q=eval(input())

for string in operate:
    op=int(string.split()[0])
    l=int(string.split()[1])-1
    r=int(string.split()[2])-1
    temp=arr[l:r+1]
    temp.sort(reverse=True if op==1 else False)
    arr[l:r+1]=temp.copy()

print(arr[q-1])
