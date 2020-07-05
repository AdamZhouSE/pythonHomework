num = int(input())
numberStr = input().split()


def str_list_to_int_list(str_list):
    int_list = []
    for c in str_list:
        int_list.append(int(c))
    return int_list


numbers=str_list_to_int_list(numberStr)
numbers.sort(reverse=True)
number=''
count0=0
count5=0
for n in numbers:
    number=number+str(n)
    if n==0:
        count0+=1
    else:
        count5+=1
res=''
for i in range(count5//9):
    res=res+'555555555'
for i in range(count0):
    res=res+'0'
if res=='':
    print(-1)
elif int(res)%90!=0:
    print(-1)
else:
    print(int(res))