n=int(input())
numberStr = input().split()


def str_list_to_int_list(str_list):
    int_list = []
    for c in str_list:
        int_list.append(int(c))
    return int_list


numbers=str_list_to_int_list(numberStr)
numbers.sort()
res=0
for i in range(n//2):
    res=res+(numbers[i]+numbers[n-1-i])**2
print(res)