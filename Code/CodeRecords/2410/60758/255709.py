a=list(map(int,input().split(",")))
diff=int(input())
max_len=1
for i in range(0,len(a)):
    current=a[i]
    current_len=1
    for j in range(i+1,len(a)):
        if(a[j]==current+diff):
            current_len+=1
            current=a[j]
    max_len=max(current_len,max_len)
print(max_len)