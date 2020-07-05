def insert_sort(s):
    for i in range(len(s)):
        loc=find_loc(s,i,s[i])
        temp=s[i]
        for j in range(i,loc,-1):
            s[j]=s[j-1]
        s[loc]=temp
        
def find_loc(s,i,ele):
    if i==0 or ele<s[0]:
        return 0
    elif i==1:
        return 1
    else:
        for j in range(0,i-1):
            if s[j]<=ele<=s[j+1]:
                return j+1
        return i
    
a=eval(input())
insert_sort(a)
print(a)