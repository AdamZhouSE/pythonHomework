a=input()
b=input()
count=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)+1):
        for k in range(0,len(b)):
            if k+j-i<=len(b):
                if a[i:j]==b[k:k+j-i]:
                    count=count+1
print(count,end="")