tup=eval(input())
repo=[]
for num in tup:
    if num not in repo:
        repo.append(num)
    else:
        print(num)
        break