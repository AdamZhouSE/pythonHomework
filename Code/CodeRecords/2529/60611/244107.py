source=str(input())
tag=0
for i in range(32):
    if sorted(source)==sorted(str(2**i)):
        print("true")
        tag=1
        break
if tag==0:
    print("false")
