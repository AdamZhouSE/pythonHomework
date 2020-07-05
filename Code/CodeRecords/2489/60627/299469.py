l = eval(input())
a = int(input())
b = int(input())
i=0
for i in range(len(s)):
    for j in range(len(s)):
        if a<=sum(l[i:j])<=b:
            i += 1
print(i)