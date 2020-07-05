num=int(input())
planes=[0]*100
for i in range(num):
    temp=[int(x) for x in input().split(",")]
    for j in range(temp[0]-1,temp[1]):
        planes[j]+=temp[2]
end=int(input())
print(planes[0:end])