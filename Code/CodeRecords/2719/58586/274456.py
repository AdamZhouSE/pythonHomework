nums=int(input())
container=[]
for i in range(nums):
    operator=input().split(" ")
    if operator[0]=="A":
        left,right=int(operator[1]),int(operator[2])
        count=0
        delete=[]
        for c in container:
            if not (c[1]<left or c[0]>right):
                count+=1
                delete.append(c)
        for c in delete:
            container.remove(c)
        container.append((left,right))
        print(count)
    elif operator[0]=="B":
        print(len(container))