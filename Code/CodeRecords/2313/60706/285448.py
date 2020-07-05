str1=input().split(' ')
n=int(str1[0])
root=int(str1[1])
ans1='true'
ans2='true'
for i in range(n):
    list1=input().split(' ')
    fa=int(list1[0])
    lch=int(list1[1])
    rch=int(list1[2])
    if (lch==0 and rch!=0) or (lch!=0 and rch==0):
        ans2='false'
    if lch>fa or fa>rch:
        ans1='false'
print(ans1)
print(ans2)