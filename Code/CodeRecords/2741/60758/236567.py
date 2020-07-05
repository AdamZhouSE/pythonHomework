a=input()
b=eval(a)
longest=0
current_len=1
for i in range(1,len(b)):
    longest=max(longest,current_len)
    if(b[i]>b[i-1]):
        current_len+=1
    else:
        current_len=1
longest=max(longest,current_len)
print(longest)