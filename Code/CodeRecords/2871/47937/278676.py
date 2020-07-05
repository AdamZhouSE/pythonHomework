n=input()

a=input().split(" ")

#print(a)

num_of_two=0
num_of_one=0

i=0

while i<len(a):
    if(a[i]=='2'):
        num_of_two+=1
    if(a[i]=='1'):
        num_of_one+=1
    i=i+1

if(num_of_two>num_of_one):
    print(num_of_one)
else:
    print(int(num_of_two+(num_of_one-num_of_two)/3))
