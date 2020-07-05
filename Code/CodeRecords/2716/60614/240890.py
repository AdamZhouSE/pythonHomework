stopWord = ']'
image = ''
for line in iter(input, stopWord):
    image += line + '\n'
image += ']\n'
print(eval(image))