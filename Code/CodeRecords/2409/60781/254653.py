chips=input()
chips=chips.split(",")
chips = list(map(int, chips))
odd=0

for i in chips:
    if i%2==1:
        odd+=1
even=len(chips)-odd
print(min(odd,even))