book_and_time=input().split()
book=int(book_and_time[0])
times=int(book_and_time[1])
timeWillUseStr=input().split()


def str_list_to_int_list(str_list):
    int_list = []
    for c in str_list:
        int_list.append(int(c))
    return int_list


timeWillUse=str_list_to_int_list(timeWillUseStr)
count=0
counts=[]

for i in range(book):
    remindTime = times
    count = 0
    for j in range(i,book):
        if remindTime >= timeWillUse[j]:
            remindTime -= timeWillUse[j]
            count += 1
    counts.append(count)
print(max(counts))