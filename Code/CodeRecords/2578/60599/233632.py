s=input()
arr=[]
num=int(input())
for i in range(len(s)):
    arr=list(map(int, s.split(',')))
sum = 0
for i in range(max(arr)+1):
    if(i==0):continue
    for k in arr:
        if(k<i):
            sum=sum+1
        elif(k%i==0):
            sum += k/i
        else:sum += int(k/i) + 1
    if(sum<=num):
        print(i)
        exit()
    sum = 0
print(max(arr))