a=eval(input())
#print(a)
end=[]

i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        end.append(int(a[i][j]))
        j=j+1
    i=i+1
print(sorted(end))