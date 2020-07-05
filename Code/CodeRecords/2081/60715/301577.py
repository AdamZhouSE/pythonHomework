s=input("")
t=input("")
count=0
for index in range(len(s)-len(t)+1):
    if s[index:index+len(t)] == t:
        count+=1
print(count,end='')