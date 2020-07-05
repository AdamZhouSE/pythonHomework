n_and_k = input().split()
n=int(n_and_k[0])
k=int(n_and_k[1])
numberStr=input().split()


def str_list_to_int_list(str_list):
    int_list = []
    for c in str_list:
        int_list.append(int(c))
    return int_list



res=0
for number in numberStr:
    count=0
    for c in number:
        if c=='4' or c=='7':
            count+=1
    if count<=k:
        res+=1
print(res)