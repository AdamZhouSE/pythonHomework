s=input()
arr=[]
num=int(input())
for i in range(len(s)):
    arr=list(map(int, s.split(',')))
if(arr[0]>num):
    print(0)
    exit()
for i in range(len(arr)-1):
    if(arr[i]==num):
        print(i)
        exit()
    elif(arr[i]<num and num<arr[i+1]):
        print(i+1)
        exit()
print(len(arr))
