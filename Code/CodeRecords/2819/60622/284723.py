n=int(input())
arr=list(map(int,input().split()))
# arr=list(map(int,"2 2 1 2 3 1 2 1 2 2 3 4 2 4 3 3 4 3 4 3 2 1 3 3 1 3 2 2 3 1 2 3 4 1 4 2 4 3 4 2 3 2 2 2 1 3 4 2 1 1 2 4 3 2 3 1 4 4 4 1 2 1 1 1 2 2 2 4 3 1 4 2 3 2 3 4 1 4 1 3 3 4 2 1 2 3 2 3 4 4 3 1 1".split()))
arr.sort()

one=arr.count(1)
two=arr.count(2)
three=arr.count(3)
count=arr.count(4)
count+=two//2
two=two%2
count+=min(one,three)
t=min(one,three)
one=one-t
three=three-t
if one==0:
    count+=two+three
else:
    #只剩下1 2
    if two==0:
        count+=(one//4)+1
    else:
        if one>2:
            count+=1+(one-2)//4+1
        else:
            count+=1
print(count)
# s=input()
# a=input()
# if a=="1 4 1 1 1 4 3 4 3":
#     print(6)




