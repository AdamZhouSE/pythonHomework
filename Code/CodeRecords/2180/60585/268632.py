s1=input()
s2=input()
n1=len(s1)
n2=len(s2)
count=0
for i in range(n1):
    for j in range(i+1,n1+1):
        temp=s1[i:j]
        step=j-i
        for k in range(n2-step+1):
            if s2[k:k+step]==temp:
                count+=1
print(count,end='')