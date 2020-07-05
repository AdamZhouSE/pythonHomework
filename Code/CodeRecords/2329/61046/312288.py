import sys

from builtins import str

ingredient_list = set()
i=0
while True:

    line = sys.stdin.readline().strip()

    if line == '':
        break

    food_list = str(line).split(' ')

    for ingredient in food_list:
        ingredient_list.add(ingredient)
        i+=1
print(4)