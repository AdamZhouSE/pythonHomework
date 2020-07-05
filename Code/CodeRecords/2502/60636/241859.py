number=int(input())
true_list=input().split(" ")
now_list=input().split(" ")
count=0
for i in range(number):
    now_list[now_list.index(true_list[i])]=i
    true_list[i]=i
for a in range(len(now_list)):
    for x in now_list[a:]:
        if(now_list[a]>x):
            count=count+1
print(count)