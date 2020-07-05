num = int(input())
numberStr = input().split()


def str_list_to_int_list(str_list):
    int_list = []
    for c in str_list:
        int_list.append(int(c))
    return int_list
swap=[]
count=0
check=0
numbers=str_list_to_int_list(numberStr)
numbersSort=[]+numbers
numbersSort.sort()
for i in range(num):

    if numbers==numbersSort:
        print(count)
        check=1
        break
    swap.append(numbers[len(numbers) - 1])
    numbers=swap[len(swap)-1:]+numbers
    del numbers[len(numbers)-1]
    count+=1


if check==0:
    print(-1)