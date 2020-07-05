num=int(input())
for k in range(num):
    s=input()
    left=0
    right=[]
    for i in range(len(s)):
        if s[i]=='(':
            left=left+1
            right.append(left)
            print(left,end=" ")
        elif s[i]==')':
            print(right[len(right)-1],end=" ")
            right=right[:len(right)-1]
        else:
            pass
    print("")