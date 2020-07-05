string=input().split(" ")
lock=int(string[0])
key=int(string[1])
locklist=input().split(" ")
keylist=input().split(" ")
lock1=0
lock2=0
key1=0
key2=0
for i in range(lock):
    if(int(locklist[i])%2==1):
        lock1+=1
    else:
        lock2+=1
for i in range(key):
    if(int(keylist[i])%2==1):
        key1+=1
    else:
        key2+=1
count=0
if(lock1<key2):
    count+=lock1
else:
    count+=key2
if(lock2<key1):
    count+=lock2
else:
    count+=key1
print(count)