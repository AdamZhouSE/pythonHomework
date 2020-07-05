def judge(string):
    m=string[0]
    n=string[len(string)-1]
    count=0
    while count<len(string) and string[count]==m:
        count=count+1
    while count<len(string) and string[count]==n:
        count=count+1
    if count==len(string):
        return True
    return False
string=input()
window_length=1
list=[]
while window_length<=len(string):
    for i in range(len(string)-window_length+1):
        if list.count(string[i:i+window_length])==0:
            list.append(string[i:i + window_length])
    window_length=window_length+1
count=0
for item in list:
    if judge(item):
        count=count+1
if count==1:
    print(0)
else:
    print(count)