line=list(map(int,input().split(" ")))
n=line[0]
m=line[1]
arr=[]
for i in range(n):
    arr.append(input())
for i in range(m):
    line = list(map(int, input().split(" ")))
    start=line[0]-1
    end=line[1]-1
    temp="aaaaaaaaaaaaaaa"
    for j in range(start,end+1):
        string=arr[j]
        for k in range(min(len(temp),len(string))):
            if temp[k]>string[k]:
                break
            elif string[k]>temp[k]:
                temp=string
                break
    print(temp)
