t=int(input())
while t>0:
    t=t-1
    s=input()
    left=0
    num=0
    temp=[]
    for item in s:
        if item=='(':
            num=num+1
            temp.append(left)
            left=num
            print(num,end=' ')
        elif item==')':
            print(left,end=' ')
            left=temp[len(temp)-1]
            temp.remove(left)
        else:
            continue
    print()