n=int(input())
li=[]
for i in range(n):
    arr=list(eval(input()))
    for j in range(n):
        li.append(arr[j])
print(sorted(li)[int(input())-1])