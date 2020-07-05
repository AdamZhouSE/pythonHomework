n=int(input())
boys=input().split(' ');boys=[int(x) for x in boys]
m=int(input())
girls=input().split(' ');girls=[int(x) for x in girls]
boys.sort();girls.sort()
count1=0
for i in range(len(boys)):
    #rec=len(boys)
    for j in range(len(girls)):
        if len(girls)==0:
            break
        if boys[i]+1 >= girls[j] >= boys[i]-1:
            count1+=1
            del girls[j]
            break
    #if rec==len(boys):
     #   del boys[i]
print(count1)