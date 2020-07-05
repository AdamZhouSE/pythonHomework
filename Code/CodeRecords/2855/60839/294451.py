def judge(x,y,lis):
    count=0
    if x>0 and x<len(lis)-1 and y>0 and y<len(lis)-1:
        if lis[x][y-1]=="o":
            count+=1
        if lis[x][y+1]=="o":
            count+=1
        if lis[x-1][y]=="o":
            count+=1
        if lis[x+1][y]=="o":
            count+=1
    elif x==0 and y==0:
        if lis[0][1]=="o":
            count+=1
        if lis[1][0]=="o":
            count+=1
    elif  x==len(lis)-1 and y== len(lis)-1:
        if lis[len(lis)-1][len(lis)-2]=="o":
            count+=1
        if lis[len(lis)-2][len(lis)-1]=="o":
            count+=1
    elif x == 0 and y == len(lis)-1:
        if lis[0][len(lis)-2] == "o":
            count += 1
        if lis[1][len(lis)-1] == "o":
            count += 1
    elif x == len(lis) - 1 and y == 0:
        if lis[len(lis) - 1][1] == "o":
            count += 1
        if lis[len(lis) - 2][0] == "o":
            count += 1
    else:
        if x==0:
            if lis[1][y]=="o":
                count+=1
            if lis[0][y+1]=="o":
                count+=1
            if lis[0][y-1]=="o":
                count+=1
        elif y==0:
            if lis[x][1]=="o":
                count+=1
            if lis[x+1][0]=="o":
                count+=1
            if lis[x-1][0]=="o":
                count+=1
        elif x==len(lis)-1:
            if lis[len(lis)-2][y]=="o":
                count+=1
            if lis[len(lis)-1][y-1]=="o":
                count+=1
            if lis[len(lis)-1][y+1]=="o":
                count+=1
        elif y==len(lis)-1:
            if lis[x][len(lis)-2]=="o":
                count+=1
            if lis[x-1][len(lis)-1]=="o":
                count+=1
            if lis[x+1][len(lis)-1]=="o":
                count+=1
    return True if count%2==0 else False

n=int(input())
lis=[]
for i in range(0,n):
    lis.append(list(input()))
if len(lis)==1:
    print("YES")
else:
    ans=True
    for i in range(0,n):
        for j in range(0,n):
            if not judge(i,j,lis):
                ans=False
    print("YES" if ans else "NO")