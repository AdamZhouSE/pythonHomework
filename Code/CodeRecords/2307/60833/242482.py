lines = []
while True:
    try:
        lines.append(input())
    except:
        break
count=int(lines.pop(0))
for i in range(0,count):
    num=int(lines[i*2])
    str_list=list(lines[i*2+1].split(" "))
    result=-1
    target=num/2
    for j in range(0,num):
        temp=str_list.count(str_list[j])
        if temp>target:
            result=str_list[j]
            break
    print(result)