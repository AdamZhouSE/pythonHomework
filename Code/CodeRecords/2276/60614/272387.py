rows=int(input())
columns=int(input())
first=int(input())
second=int(input())
ans=[[first,second]]
last='U'
steps=0

while len(ans)<rows*columns:
    if last=='U':
        steps+=1
        last='R'
        for i in range(steps):
            second+=1
            if first<rows and second<columns and first>=0 and second>=0:
                ans.append([first,second])
    if last=='R':
        last='D'
        for i in range(steps):
            first+=1
            if first<rows and second<columns and first>=0 and second>=0:
                ans.append([first,second])
    if last=='D':
        steps+=1
        last='L'
        for i in range(steps):
            second-=1
            if first<rows and second<columns and first>=0 and second>=0:
                ans.append([first,second])
    if last=='L':
        last='U'
        for i in range(steps):
            first-=1
            if first<rows and second<columns and first>=0 and second>=0:
                ans.append([first,second])
print(ans)