num_1=list(map(int,input().replace('[','').replace(']','').split(',')))
num_2=list(map(int,input().replace('[','').replace(']','').split(',')))

if len(num_1)<len(num_2):
    small=list(set(num_1))
    large=num_2
else:
    small=list(set(num_2))
    large=num_1

for i in small:
    if i not in large:
        small.remove(i)
small.sort(reverse=False)
print(small)