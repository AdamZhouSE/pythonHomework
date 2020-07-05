num=input().split()
array=input().split()
def judge(string,num):
    for i in range(len(string)):
        if string[i]=='4' or string[i]=='7':
            num=num-1
    return num>=0
count=0
for item in array:
    if judge(item,int(num[1])):
        count=count+1
print(count)