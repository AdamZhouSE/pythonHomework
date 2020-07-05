num_list=list(map(int,input().split(",")))
k=int(input())
if (max(num_list)-min(num_list))<=2*k:
    print(0)
else:
    print(str(max(num_list)-min(num_list)-2*k))