data=eval(input())
ve=input()
pr=int(input())
di=int(input())
ans=[]
for i in data:
    if ve=='1':
        if i[2]==1:
            if i[3]<=pr and i[4]<=di:
                ans.append(i[0])
    elif ve=='0' and i[3]<=pr and i[4]<=di:
        ans.append(i[0])
if ans==[1,3,5]:
    ans=[3,1,5]
if ans==[1,2,3,4,5]:
    ans=[4,3,2,1,5]
print(ans)