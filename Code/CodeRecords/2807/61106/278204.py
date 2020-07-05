def odd_even(list):
    odd,even=0,0
    for i in range(len(list)):
        if list[i]%2==1 :
            odd += 1
        else:
            even += 1
    return [odd,even]

n,m=map(int,input().split())
nbox=list(map(int,input().split()))
nkey=list(map(int,input().split()))
box=odd_even(nbox)
key=odd_even(nkey)
print(min(box[0],key[1])+min(box[1],key[0]))