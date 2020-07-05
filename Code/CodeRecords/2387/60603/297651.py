list=input().split(" ")
num=int(list[0])
time=int(list[1])
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])

for z in range(time):
    string=input().split(" ")
    isreverse=int(string[0])
    left=int(string[1])-1
    right=int(string[2])-1
    sublist=[]
    if(isreverse==0):
        sublist=list[left:right+1]
        sublist.sort()
    else:
        sublist=list[left:right+1]
        sublist.sort(reverse=True)

    for i in range(left,right+1):
        list[i]=sublist[i-left]
rank=int(input())
print(list[rank-1])