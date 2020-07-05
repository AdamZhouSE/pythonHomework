num_list=list(map(int,input().split(",")))
def judgeTriangle(a,b,c):
    if a+b>c:
        if a+c>b:
            if b+c>a:
                return True
    return False
length=len(num_list)
max_c=0
for i in range(length-2):
    for j in range(i+1,length-1):
        for k in range(j+1,length):
            if judgeTriangle(num_list[i],num_list[j],num_list[k]):
                max_c=max(max_c,num_list[i]+num_list[j]+num_list[k])
print(max_c)

