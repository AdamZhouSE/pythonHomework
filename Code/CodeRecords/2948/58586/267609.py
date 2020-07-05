names=input()
ST=int(input())
src=""
for c in names:
    src+=str(ord(c)-65+ST)
arr=[int(c) for c in src]
length=len(arr)
for round in range(len(arr)-3):
    for j in range(length-1):
        arr[j]=(arr[j]+arr[j+1])%10
    length-=1
if arr[0:3]==[1,0,0]:
    print(100,end="")
else:
    print((arr[0]+arr[1])%10*10+(arr[1]+arr[2])%10,end="")



