n=int(input())
num_list=list(map(int,input().split(" ")))
a=num_list.index(max(num_list))+1
b=num_list.index(min(num_list))+1
list1=[]
list1.append(n-a)
list1.append(n-b)
list1.append(b-1)
list1.append(a-1)
print(max(list1))