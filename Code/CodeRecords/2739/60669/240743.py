x=input()
n=int(x.split(", ")[1])
k=int(x.split(", ")[0])

result=[]
if n<=(1+2+9):
    for i in range(1,8):  #(1,7)
        for j in range(1+i,9):   #(2,8)
            if (n-i-j)>j:
                result.append([i,j,n-i-j])
            else:
                break
print(result)