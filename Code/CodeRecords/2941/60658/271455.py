gpa = {"A":4,"B":3,"C":2,"D":1,"E":0,"F":0}
n = int(input())
allgpa = input()
ans = 0
for i in allgpa:
    ans+=gpa[i]
if ans==0:
    print(0,end="")
else:
    print("{:.14f}".format(ans/n),end="")