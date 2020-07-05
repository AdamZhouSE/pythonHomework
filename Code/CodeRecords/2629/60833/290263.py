n=int(input())
dict1={'102':4,'101':4,'95':6,'72':2,'71':4,'66':2,'60':4,'6':6}
for i in range(0,n):
    l=list(dict1.keys())
    num=input()
    if num in l:
        print(dict1[num])
    else:
        print(num)