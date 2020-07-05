li = [int(x) for x in input().split(",")]
li.sort(reverse = True)
for i in range(len(li)-2):
    if li[i]<li[i+1]+li[i+2]:
        print(sum(li[i:i+3]))
        exit()
print(0)
