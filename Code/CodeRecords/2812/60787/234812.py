n=int(input())
stu=input().split(" ")
re=[]
for i in stu:
    if int(i)>0 and (not i in re):
        re.append(i)
print(len(re))