s=input()
num=s.split(',')
t=input()
flag =0
first=-1
last=0
for i in range(len(num)):
    if(t==num[i] and flag==0):
        first = i
        flag = flag+1
    if(t==num[i]):
        last=i
if first < 0:
    print([-1,-1])
    exit()
print([first,last])