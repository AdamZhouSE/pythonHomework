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
for n in numbers:
    number=number+str(n)
    if n==0:
        count0+=1

for i in range(len(number)):
    if count0==1:
        if int(number) % 90 == 0:
            print(int(number))
            break
        number = number[1:]
    else:
        if int(number) % 90 == 0:
            print(int(number))
            break
        number = number[:len(number)-1]
        count0-=1
if '0' not in number:
    print(-1)