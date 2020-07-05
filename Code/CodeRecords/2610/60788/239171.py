from sys import stdin
def is_diff(li):
    for i in li:
        if li.count(i)>=2:
            return False
    return True

num=int(stdin.readline().strip())
for i in range(0,num):
    length=int(stdin.readline().strip())
    li=[x for x in stdin.readline().split()]
    s=0
    for j in range(1,len(li)+1):
        for k in range(0,len(li)+1-j):          
            sub_li=li[k:k+j]
            if is_diff(sub_li):
                s+=j
    print(s)
