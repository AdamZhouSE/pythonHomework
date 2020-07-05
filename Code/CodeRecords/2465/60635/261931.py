src=eval(input())
h=0
def check(num):
    count=0
    for n in src:
        if n>=num:
            count+=1
    if count >= num:
        return True
    return False
for num in range(1,len(src)+1):
    if check(num):
        h=num
print(h)