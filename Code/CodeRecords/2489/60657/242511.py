import re
arr=input()
low=input()
up=input()
low=int(low)
up=int(up)
arr=arr[1:-1]
arr=arr.split(',')
arr=[int(x) for x in arr]
con=0
if arr[0]<=low:
    con+=1
if arr[-1]<=up:
    con+=1
if sum(arr)<=up and sum(arr)>=low:
    con+=1
if(con==0):
    con=1
print(con)