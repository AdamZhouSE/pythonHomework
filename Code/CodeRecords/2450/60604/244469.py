a=input().split(',')
b=input()
#print(a)
#print(b)
res=[-1]*2
begin=-1
end=-1
for i in range(len(a)):
    if a[i]==b and begin==-1:
        begin=i
        end=i
    elif a[i]!=b and begin!=-1:
        end=i-1
        break
res[0]=begin
res[1]=end
print(res)