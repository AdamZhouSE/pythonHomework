tomato = int(input())
cheese = int(input())
combo = []
if cheese == 0 and tomato == 0:
    combo = [0,0]
else:
    for i in range(cheese+1):
        if i*4 + 2*(cheese-i) == tomato:
            combo.append(i)
            combo.append(cheese-i)
print(combo)