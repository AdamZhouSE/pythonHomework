num=int(input());
size=int(input());
U=[];
for i in range(num):
    U.append(int(input()));
U.sort(key=None,reverse=True);
count=0;
result=0;
while result<size:
    result=result+U[count];
    count+=1;
print(count);