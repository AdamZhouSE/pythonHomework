def check(list):
    l=len(list)
    for i in range(1,l-1):
        if i%2==1:
            if not(list[i-1]>=list[i]and list[i]<=list[i+1]):
                return False
        if i%2==0:
            if not(list[i-1]<=list[i]and list[i]>=list[i+1]):
                return False
    return True
def swep(list,a,b):
    list[a]=list[a]+list[b]
    list[b]=list[a]-list[b]
    list[a]=list[a]-list[b]
    return list
N=int(input())
for n in range(0,N):
    l=int(input())
    temp=input().split(" ")
    list=[]
    for item in temp:
        list.append(int(item))
    while(check(list)==False):
        for i in range(1,l):
            if i % 2 == 1:
                if not list[i - 1]>=list[i]:
                    swep(list,i-1,i)
                    break
                if not list[i+1]>=list[i]:
                    swep(list,i+1,i)
                    break
            if i%2==0:
                if not list[i-1]<=list[i]:
                    swep(list,i-1,i)
                    break
                if not list[i+1]<=list[i]:
                    swep(list,i+1,i)
                    break
    for i,item in enumerate(list):
        if i !=len(list)-1:
            print(item,end=" ")
        else:
            print(item)