data=eval(input())
perimeter=0
for i in range(len(data)):
    for j in range(i+1,len(data)):
        for k in range(j+1,len(data)):
            edge1=data[i]
            edge2=data[j]
            edge3=data[k]
            if edge1+edge2>edge3 and edge1+edge3>edge2 and edge2+edge3>edge1:
                perimeter1=edge1+edge2+edge3
                if perimeter1>perimeter:
                    perimeter=perimeter1
print(perimeter)