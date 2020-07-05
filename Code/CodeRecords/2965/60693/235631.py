k_m=input().split()  # input k & m
k=int(k_m[0])
m=int(k_m[1])
# print(k,m)
oristr=input()  # input original string
op_times=int(input())  # input operation times
tmpstr=oristr
for x in range(op_times):
    op=input().split()  # input every operations
    # print(op)
    copy_start=int(op[0])
    copy_end=int(op[1])
    paste_index=int(op[2])
    copy_str=tmpstr[copy_start:copy_end]
    # print(copy_str)
    tmpstr=copy_str.join([tmpstr[:paste_index],tmpstr[paste_index:]])  # paste
    tmpstr=tmpstr[:m]  # the string max length
    # print(tmpstr)
print(tmpstr[:k],end='')
