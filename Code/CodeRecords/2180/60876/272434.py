str1=input()
str2=input()
len1=len(str1)
len2=len(str2)
sum=0
for start in range(0,len1):
    for end in range(start,len1):
        temp=str1[start:end+1]
        l=list(str2)
        length=len(temp)
        while temp in "".join(l):
            ind=("".join(l)).index(temp)
            del l[ind:ind+length]
            sum+=1
print(sum,end="")