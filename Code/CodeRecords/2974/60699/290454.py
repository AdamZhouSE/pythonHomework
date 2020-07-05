k=int(input())
str1=input()
def huiwen(s):
    if len(s)%2==0:
        return False
    start=0
    end=len(s)-1
    while start<end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True

def all(s):
    set1=set()
    for i in range(1,k+1):
        for j in range(0,k-i+1):
            set1.add(s[j:j+i])
    return len(set1)-1

def pos_hui(s):
    set1 = set()
    for i in range(1, k + 1, 2):
        for j in range(0, k - i + 1):
            if huiwen(s[j:j + i]):
                set1.add(s[j:j + i])
    return len(set1)

max1=0
for i in range(1,k-1):
    A=pos_hui(str1[0:i])
    B=all(str1[i:])-pos_hui(str1[i:])
    max1=max(max1,A*B)
print(max1)