arr=eval(input())
count=0
for i in range(len(arr)):
    a=arr[:i+1]
    if max(a)==i:
        count+=1
print(count)