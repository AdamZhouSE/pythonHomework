length=eval(input())
length.sort()
ptr=0
res=0
while(ptr<len(length)-2 and length[ptr]>=length[ptr+1]+length[ptr+2]):
    ptr+=1
if(length[ptr]<length[ptr+1]+length[ptr+2]):
    res=length[ptr]+length[ptr+1]+length[ptr+2]
print(res)