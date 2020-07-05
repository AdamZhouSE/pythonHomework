n = int(input())
distance = list(map(int,input().split()))
st = list(map(int,input().split()))
st.sort()
min1 = 0
min2 = 0
min3 = 0
for i in range(st[0]-1,st[1]-1):
    min1 = min1+distance[i]
for i in range(0,st[0]-1):
    min2 = min2+distance[i]
for i in range(st[1]-1,n):
    min3 = min3+distance[i]
print(min1 if min1<min2+min3 else min2+min3)
    