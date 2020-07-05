R=int(input())
C=int(input())
i=int((input()))
j=int(input())
result=[[i,j]]
n=1#n%4=1——向东走int(n/4)*2+1步；n%4=2——向南走int((n-1)/4)*2+1步;n%4=3——向西走int(n/2)+1步；n%4=0——向北走n/2步
while len(result)<R*C:
    if n%4==1:
        step=int(n/4)*2+1
        while step>0:
            j=j+1
            if (i >= 0 and i < R) and (j >= 0 and j < C):
                result.append([i, j])
            step=step-1
    elif n%4==2:
        step=int((n-1)/4)*2+1
        while step > 0:
            i = i + 1
            if (i >= 0 and i < R) and (j >= 0 and j < C):
                result.append([i, j])
            step = step - 1
    elif n%4==3:
        step=int(n/2)+1
        while step > 0:
            j = j - 1
            if (i >= 0 and i < R) and (j >= 0 and j < C):
                result.append([i, j])
            step = step - 1
    elif n%4==0:
        step=int(n/2)
        while step > 0:
            i = i - 1
            if (i >= 0 and i < R) and (j >= 0 and j < C):
                result.append([i, j])
            step = step - 1
    n=n+1
print(result)

