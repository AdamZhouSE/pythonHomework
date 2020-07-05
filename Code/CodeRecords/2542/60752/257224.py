lst=eval(input())
list.sort(lst)
max=1
start=0
for i in range(len(lst)-1):
    if lst[i+1]-lst[i]!=1:
        if max<i-start+1:max=i-start+1
        start=i+1
    i+=1
print(max)
