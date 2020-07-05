n=int(input())
arr=input().split(" ")
arr=list(int(a) for a in arr)
arr=set(arr)
if(0 in arr):
    arr.remove(0)
print(len(arr))
