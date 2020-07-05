size=int(input())
for j in range(size):
    list0=input().split()
    str1=list0[0]+list0[1]
    list1=list(set(list(str1)))
    print(len(list1))