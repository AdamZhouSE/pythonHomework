n =int(input())
num_list=list(map(int,input().split()))
num_list.sort()
amount=1
j=1
def sum_1(list_1):
    element=0
    for  i in list_1:
        element+=i
    return element
while j<n:
    if num_list[j]>=sum_1(num_list[:j]):
        amount+=1
        j+=1
    else:
        del num_list[j]
        n-=1
print(amount)
    
    
              