l = eval(input())
a = int(input())
b = int(input())
i=0
for i in range(len(l)):
    for j in range(len(l)):
        if a<=sum(l[i:j])<=b:
            i += 1
print(i)