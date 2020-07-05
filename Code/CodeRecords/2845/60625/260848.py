computer=int(input())
aiStr=input().split()
biStr=input().split()


def str_list_to_int_list(str_list):
    int_list = []
    for c in str_list:
        int_list.append(int(c))
    return int_list

check=0
ai=str_list_to_int_list(aiStr)
bi=str_list_to_int_list(biStr)
for a in range(len(ai)):
    for b in range(len(bi)):
        if ai[a]<=ai[b] and bi[a]>=bi[b]:
            check=1
if check==0:
    print('Poor Alex')
else:
    print('Happy Alex')