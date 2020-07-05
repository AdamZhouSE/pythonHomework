n=int(input())
l_input=[]
for i in range(n):
    l=input().split()
    l_input.append(int(l[0])+int(l[1]))
l_input.sort()
print(l_input[-1])