n=int(input())
for i in range(n):
    a=input()
    letter_list1=set(input().split())
    letter_list2=list(input().split())
    res=0
    for element in letter_list1:
        if letter_list2.count(element)>0:
            res+=1
    print(res) 
   