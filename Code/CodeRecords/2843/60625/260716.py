n=int(input())
numbers=input().split()


def str_list_to_int_list(str_list):
    int_list = []
    for c in str_list:
        int_list.append(int(c))
    return int_list


newNumbers=[]
for index in range(n):
    if index==n-1:
        newNumbers.append(numbers[index])
        break
    newNumbers.append(str(int(numbers[index])+int(numbers[index+1])))
print(' '.join(newNumbers))