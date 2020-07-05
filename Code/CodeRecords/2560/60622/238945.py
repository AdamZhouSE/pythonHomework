def print_ID():
    num=int(input())
    arr=input().split()
    num_To_Delete=int(input())
    while(len(arr)!=(num-num_To_Delete)):
        #删除出现次数最少的元素
        delete(arr)
    set_ans=set(arr)
    print(len(set_ans),end='')
def delete(list):
    count=list.count(list[0])
    ans=list[0]
    for n in list:
        if list.count(n)<count:
            count=list.count(n)
            ans=n
    list=list.remove(ans)
    return list



num=int(input())
for i in range(num):
    print_ID()
    print()