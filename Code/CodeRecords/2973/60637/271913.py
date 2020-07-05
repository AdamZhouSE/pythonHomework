string=input()
map=[]
for i in range(len(string)-7):
    map.append("".join(sorted(list(string[i:i+8]))))

code_nums=(int)(input())
sum=0
for i in range(code_nums):
    code=input()
    sorted_code="".join(sorted(list(code)))
    for i in map:
        if(i==sorted_code):
            sum+=1
print(sum)