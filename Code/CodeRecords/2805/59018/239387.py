n=int(input())
a=[]
info=input().split(' ')
list=[int(y) for y in info]

  
for i in range(n):
    for j in range(i,n):
        if list[i:j+1]==sorted(list[i:j+1]):
            a.append(j-i+1)
        else:
            break

print(max(a))

    