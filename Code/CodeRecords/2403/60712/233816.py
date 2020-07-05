candies = int(input())
x=0
num_people = int(input())
list1 = [0]*num_people
while candies>0:
    if candies>(x+1):
        list1[x%num_people] = list1[x%num_people]+x+1
        candies = candies-(x+1)
    else:
        list1[x%num_people]=list1[x%num_people]+candies
        candies=0
    x=x+1
print(list1)