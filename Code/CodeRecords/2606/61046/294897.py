test=list(input())
num=int(input())
lst=[]
count={}
test.pop(0)
test.pop(-1)
temp=str("".join(test))
lst=temp.split(",")
lst=list(map(int,lst))
if num not in lst:
    print(-1)
else:
    print(lst.index(num))